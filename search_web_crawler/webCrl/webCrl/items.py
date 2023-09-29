# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderwebItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    keywords = scrapy.Field()


class ImagegSpiderItem(scrapy.Item):
    url = scrapy.Field()
    image_url = scrapy.Field()
    image_dsc = scrapy.Field()
    image_possible_relation = scrapy.Field()


class PageContentItem(scrapy.Item):
    url = scrapy.Field()
    page_content = scrapy.Field()

