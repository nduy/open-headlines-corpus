from scrapy.crawler import CrawlerProcess
import webspider;
import time

process = CrawlerProcess();
process.crawl(webspider.GoogleSpider());
process.crawl(webspider.TimeSpider());
process.crawl(webspider.WTJSpider());
process.crawl(webspider.WPSpider());
process.crawl(webspider.NYTSpider());
process.start();

