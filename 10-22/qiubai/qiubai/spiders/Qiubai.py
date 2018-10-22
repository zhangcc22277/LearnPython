# -*- coding: utf-8 -*-
import scrapy
from items import QiubaiItem

class QiubaiSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    # 应该返回一个值，解析的所有数据，必须返回一个可以迭代的对象
    def parse(self, response):
        author_list = response.xpath('//div[starts-with(@class,"author")]')
        #print(author_list)

        item = []
        # selector对象可以继续使用xpath进行解析操作
        for author_node in author_list:
            item = {
                'naem': author_node.xpath('.//h2/text()').extract_first().strip('/n'),
                'age' : author_node.xpath('./div/text()').extract_first(),
                'img_url' :'http:'+author_node.xpath('.//img@src').extract_first(),
            }
            #字典的键必须和items里面声明的键一致
            items.append(item)
        #不写不会报错，意味着你没有把数据提交给引擎，引擎也不会提交各管道，数据就不会被管道保存
        return items

