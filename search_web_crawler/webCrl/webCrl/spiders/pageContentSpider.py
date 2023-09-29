import scrapy
from scrapy.linkextractors import LinkExtractor
import re
from  ..items import PageContentItem
from scrapy.http import HtmlResponse
from ..data import user_agent_list, allowed_donains, Urls_to_crawl
from random import randint


class PagecontentspiderSpider(scrapy.Spider):
    name = 'page_content'
    collection_name = 'page_content'
    allowed_domains = allowed_donains
    start_urls = Urls_to_crawl

    def parse(self, response, sel=None):
        # Clean the HTML to exclude JavaScript and CSS
        cleaned_html = self.remove_js_css(response)

        cleaned_response = HtmlResponse(url=response.url, body=cleaned_html, encoding='utf-8')

        # Extract all text from the web page
        page_text = ' '.join(cleaned_response.xpath("//body//text()").extract()).strip()

        # urlHTML = requests.get(response.url)
        print(page_text)
        # data = nltk.clean_html(urlHTML)
        cleaned_page_content = self.clean_text(page_text)

        pageItem = PageContentItem()
        pageItem['url'] = response.url
        pageItem['page_content'] = cleaned_page_content

        yield pageItem

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

    def clean_text(self, text):
        # Remove leading and trailing whitespace and newlines
        cleaned_text = text.strip()

        # Remove extra whitespace and newlines
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

        return cleaned_text
