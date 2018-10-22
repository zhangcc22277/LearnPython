#coding =utf-8
#"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"

import urllib.request
import urllib.parse


url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}

format={
    'start':'0',
    'limit':'20'
}

data = urllib.parse.urlencode(format).encode('utf-8')
request = urllib.request.Request(url,data=data,headers=headers)
response = urllib.request.urlopen(request).read()
print(response)