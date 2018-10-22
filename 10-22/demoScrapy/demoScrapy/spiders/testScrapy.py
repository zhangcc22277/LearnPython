#coding =utf-8

import scrapy

class TestScrapy(scrapy.Spider):
    name = 'test1'
    allowed_domains = ["http://www.itcast.cn/"]
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]

    def parse(self, response):
        print(response.text)