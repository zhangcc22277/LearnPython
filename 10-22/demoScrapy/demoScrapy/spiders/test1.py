#coding =utf-8
name = 'test3'
allowed_domains = ["www.hezhezu.com/"]
start_urls = ["http://www.hezhezu.com/list.asp?id=83"]


def parse(self, response):

   res_resp= response.xpath('/html/body/table[5]/tbody/tr/td/table/tbody/tr/td[1]/div/a[1]')
   print(res_resp)