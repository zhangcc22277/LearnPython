#coding =utf-8

import urllib.request
import urllib.parse
url = 'http://www.baidu.com'
headers = {
	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
data = {
	'name'= 'zhangchen'
	'old':18
}
postdata = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url,postdata,headers= headers)
response = urllib.request.urlopen(request).read()
print(response)