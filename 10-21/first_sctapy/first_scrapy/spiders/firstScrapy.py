#coding =utf

import scrapy

#创建一个爬虫类
class firstScrapy(scrapy.Spider):
    name = 'ccscr'
    #允许爬虫的作用范围
    allowd_domains = ["baidu.com"]
    #爬虫的其实url
    statt_urls = ["http:/baidu.com/"]

    def parse(self, response):
        print(response.body)




