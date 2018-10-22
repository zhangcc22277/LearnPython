#coding =utf-8
import scrapy

class TestScrapy(scrapy.Spider):
    name = 'test'
    allowed_domains = ["http://www.hezhezu.com/"]
    start_urls = ["http://www.hezhezu.com/list.asp?id=83"]

    def parse(self, response):
        print(response.text)