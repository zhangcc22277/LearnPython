#coding =utf-8
#抓取超链接标签间的内容

import re
import urllib.request

url = "http://www.baidu.com/"
content = urllib.request.urlopen(url).read().decode('utf-8')

#获取完整的超链接
res1 = r"<a.*?href=.*?</a>"
urls = re.findall(res1,content)
for u in  urls:
    print(u)

#获取超链接<a>和《/a》之间的内容
res2 = r"<a.*?>(.*?)</a>"
text = re.findall(res2,content,re.S|re.M)
for t in text:
    print(t)