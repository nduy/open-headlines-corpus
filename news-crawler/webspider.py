import scrapy;
import datetime;
import HTMLParser;
from pymongo import MongoClient;
from datetime import datetime;

class TimeSpider(scrapy.Spider):
	client = MongoClient('localhost', 27017);
	db = client.rskills;
	collection = db.crawleddata;
	name = 'TimeSpider';
	start_urls = ['http://time.com'];
		
	def parse(self, response):
		for rec in response.xpath('//div/h3/a/text()').extract():
			if rec.count(' ')>=1: # At least 1 space (2 words)
				post = {"crawlerid:" : "TimeSpider","content": rec, "time" : datetime.now()};
				self.collection.insert_one(post);

			
class GoogleSpider(scrapy.Spider):
	client = MongoClient('localhost', 27017);
	db = client.rskills;
	collection = db.crawleddata;
	name = 'YahooSpider';
	start_urls = ['https://news.google.com/news?pz=1&hl=en&tab=nn&authuser=0'];
		
	def parse(self, response):
		for rec in response.xpath('//td/div/h2/a/span/text()').extract():
			if rec.count(' ')>=1: # At least 1 space (2 words)
				post = {"crawlerid:" : "GoogleSpider", "content": rec, "time" : datetime.now()};
				self.collection.insert_one(post);

class WTJSpider(scrapy.Spider):
	client = MongoClient('localhost', 27017);
	db = client.rskills;
	collection = db.crawleddata;
	name = 'WTJSpider';
	start_urls = ['http://www.wsj.com/europe'];
		
	def parse(self, response):
		for rec in response.xpath('//div/h3/a/text()').extract():
			if rec.count(' ')>=1: # At least 1 space (2 words)
				post = {"crawlerid:" : "WTJSpider","content": rec, "time" : datetime.now()};
				self.collection.insert_one(post);

class WPSpider(scrapy.Spider):
	client = MongoClient('localhost', 27017);
	db = client.rskills;
	collection = db.crawleddata;
	name = 'WPSpider';
	start_urls = ['https://www.washingtonpost.com/'];
		
	def parse(self, response):
		for rec in response.xpath('//div/div/div/div/ul/li/a/text()').extract():
			if rec.count(' ')>=1: # At least 1 space (2 words)
				post = {"crawlerid:" : "WPSpider","content": rec, "time" : datetime.now()};
				self.collection.insert_one(post);

class NYTSpider(scrapy.Spider):
	client = MongoClient('localhost', 27017);
	db = client.rskills;
	collection = db.crawleddata;
	name = 'NYTSpider';
	start_urls = ['http://www.nytimes.com/'];
		
	def parse(self, response):
		for rec in response.xpath('//li/article/h2/a/text()').extract():
			if rec.count(' ')>=1: # At least 1 space (2 words)
				post = {"crawlerid:" : "NYTSpider","content": rec, "time" : datetime.now()};
				self.collection.insert_one(post);