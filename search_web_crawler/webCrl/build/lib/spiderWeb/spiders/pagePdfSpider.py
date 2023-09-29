import scrapy
from scrapy.linkextractors import LinkExtractor
from ..data import user_agent_list
from random import randint
import re
from bs4 import BeautifulSoup
import requests
import json
import nltk
import lxml.html
import textwrap
from scrapy.loader import ItemLoader
from scrapy.http import HtmlResponse
from ..items import SpiderwebItem
from scrapy.selector import Selector


class PagepdfspiderSpider(scrapy.Spider):
    name = "pdf"
    collection_name = 'page_pdfs'
    start_urls = ['http://millardayo.com']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            if href.endswith('.pdf'):
                # sleep(1)
                yield scrapy.Request(
                    url=response.urljoin(href),
                    callback=self.save_pdf
                )

        link_extractor = LinkExtractor(unique=True, attrs='href')

        for link in link_extractor.extract_links(response):
            if link.url is not None:
                yield response.follow(link.url, callback=self.parse, headers={"User_Agent": user_agent_list[randint(0, len(user_agent_list)-1)]})

    def save_pdf(self, response):
        path = response.url.split('/')[-1]
        yield {
            "pdfTerm": path,
            "pdfUrl": response.url
        }
        self.logger.info('Saving PDF %score', path)
        with open(f'pdfFiles/{path}', 'ab') as f:
            f.write(response.body)