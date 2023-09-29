import scrapy
from scrapy.linkextractors import LinkExtractor
import re
from scrapy.http import HtmlResponse
from ..items import ImagegSpiderItem
from ..data import user_agent_list
from random import randint


class ImageSpider(scrapy.Spider):
    collection_name = 'page_images'
    name = 'image'
    allowed_domain = ['mabumbe.com']
    start_urls = ['http://mabumbe.com/']

    def parse(self, response):
        # Clean the HTML to exclude JavaScript and CSS
        cleaned_html = self.remove_js_css(response)

        # Create a new response object from the cleaned HTML
        cleaned_response = HtmlResponse(url=response.url, body=cleaned_html, encoding='utf-8')

        images = cleaned_response.css('img::attr(src)').getall()
        for image in images:
            if self.is_valid_image(image):
                image_url = response.urljoin(image)

                # Extract text before and after the image
                text_before_image = self.extract_text_before_image(cleaned_response, image)
                text_after_image = self.extract_text_after_image(cleaned_response, image)

                # Format the text
                cleaned_text = self.clean_text(text_before_image + text_after_image)

                imageItem = ImagegSpiderItem()

                imageItem['url'] = response.url
                imageItem['image_url'] = image_url
                imageItem['image_possible_relation'] = cleaned_text

                yield imageItem
        link_extractor = LinkExtractor(unique=True, attrs='href')

        for link in link_extractor.extract_links(response):
            if link.url is not None:
                yield response.follow(link.url, callback=self.parse, headers={"User_Agent": user_agent_list[randint(0, len(user_agent_list)-1)]})

    def remove_js_css(self, response):
        # Convert the response body to a string
        html_string = response.body.decode('utf-8')

        # Remove script tags and their content from the HTML
        cleaned_html = re.sub(r'<script\b[^>]*>.*?</script>', '', html_string, flags=re.DOTALL)

        # Remove style tags and their content from the HTML
        cleaned_html = re.sub(r'<style\b[^>]*>.*?</style>', '', cleaned_html, flags=re.DOTALL)

        return cleaned_html

    def extract_text_before_image(self, response, image_src):
        # Get the parent element of the image
        parent_element = response.xpath(f'//img[@src="{image_src}"]/parent::*')

        # Extract all text from elements before the image's parent element
        text_before = parent_element.xpath('preceding::text()').getall()
        return ''.join(text_before)

    def extract_text_after_image(self, response, image_src):
        # Get the parent element of the image
        parent_element = response.xpath(f'//img[@src="{image_src}"]/parent::*')

        # Extract all text from elements after the image's parent element
        text_after = parent_element.xpath('following::text()').getall()
        return ''.join(text_after)

    def clean_text(self, text):
        # Remove leading and trailing whitespace and newlines
        cleaned_text = text.strip()

        # Remove extra whitespace and newlines
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

        return cleaned_text

    def is_valid_image(self, image_url):
        # Add more image extensions if needed
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', ' ']
        return any(image_url.lower().endswith(ext) for ext in image_extensions)
