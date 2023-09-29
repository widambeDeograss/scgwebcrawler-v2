import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import SpiderwebItem
from scrapy.selector import Selector
from random import randint
from ..data import user_agent_list


class WebspiderSpider(scrapy.Spider):
    name = 'webspider'
    allowed_domains = ['mabumbe.com']
    start_urls = ['http://mabumbe.com/','']

    def parse(self, response):
        spider_item = SpiderwebItem()

        spider_item['url'] = response.url
        spider_item['title'] = response.css('title::text').get()
        spider_item['description'] = response.xpath("//meta[@name='description']/@content").get()
        spider_item['keywords'] = response.xpath("//meta[@name='keywords']/@content").get()
        # try:
        #     yield {
        #         'url': response.url,
        #         'title': response.css('title::text').get(),
        #         'description': response.xpath("//meta[@name='description']/@content").get(),
        #         'keywords': response.xpath("//meta[@name='keywords']/@content").get()
        #     }
        # except:
        #     yield {
        #         'url': response.url,
        #         'title': response.css('title::text').get(),
        #         'description': '',
        #         'keywords': ''
        #     }
        yield spider_item
        link_extractor = LinkExtractor(unique=True, attrs='href')
        print(user_agent_list)
        for link in link_extractor.extract_links(response):
            if link.url is not None:
                yield response.follow(link.url, callback=self.parse, headers={"User_Agent": user_agent_list[randint(0, len(user_agent_list)-1)]})






