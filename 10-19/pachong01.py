#coding =utf-8

from urllib.request import urlopen
import  urllib3
import urllib.reques
import urllib.request
#直接向请求的对象发送url
file  = urllib.request.urlopen("http://www.baidu.com")#访问url
data = file.read()#读取全部
dataline = file.readline()#读取一行
print(dataline)
# fhand = open("","")#将爬取的网页保存到本地
# fhand.write(data)
# fhand.close()



