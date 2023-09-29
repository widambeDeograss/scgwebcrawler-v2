# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from itemadapter import ItemAdapter
from elasticsearch import Elasticsearch


class ElasticsearchPipeline:
    def __init__(self, elasticsearch_uri, index_name):
        self.elasticsearch_uri = elasticsearch_uri
        self.index_name = index_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            elasticsearch_uri=crawler.settings.get('ELASTICSEARCH_URI'),
            index_name=crawler.settings.get('ELASTICSEARCH_INDEX', 'items')
        )

    def open_spider(self, spider):
        self.client = Elasticsearch(self.elasticsearch_uri)
        if not self.client.indices.exists(index=self.index_name):
            self.client.indices.create(index=self.index_name)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.client.index(index=self.index_name, body=dict(item))
        if hasattr(spider, 'collection_name'):
            self.index_name = spider.collection_name
        return item


class LinkedinPipeline:
    def process_item(self, item, spider):
        return item
from scrapy.exceptions import NotConfigured


class SpiderwebPipeline:
    def process_item(self, item, spider):
        return item


class MongoDBPipeline:
    collection_name = 'spider_web_page'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_URI'),
            mongo_db=crawler.settings.get('MONGODB_DB', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        if hasattr(spider, 'collection_name'):
            self.collection_name = spider.collection_name
        return item


