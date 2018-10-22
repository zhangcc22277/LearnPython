
#coding =utf-8
import scrapy


class huyalol(scrapy.Spider):
  name = "huyalol"
  start_urls = ["https://www.huya.com/g/lol"]

  def parse(self, response):
      title_list = response.xpath('//*[@id="js-live-list"]/li/a[2]/text()').extract()
      name_list = response.xpath('//*[@id="js-live-list"]/li/span/span[1]/i/text()').extract()
      for i in range(1, 11):
          print(name_list, ': ', title_list[i - 1])
