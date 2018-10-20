#coding =utf-8
import urllib.request
# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
http_handle = urllib.request.HTTPHandler()
# 调用request.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib.request.build_opener(http_handle)
# 构建 Request请求
request = urllib.request.Request("http://www.baidu.com")
# 调用自定义opener对象的open()方法，发送request请求
response = opener.open(request)
# 获取服务器响应内容

print(response.read())
