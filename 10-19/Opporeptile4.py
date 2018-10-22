#coding =utf-8
#代理服务器设置
import urllib.request
#应用场景：使用同一个IP去爬取同一个网站上的网页，久了之后会被该网站服务器屏蔽。
#解决方法：使用代理服务器。 （使用代理服务器去爬取某个网站的内容的时候，在对方的网站上，显示的不是我们真实的IP地址，而是代理服务器的IP地址）

def use_proxy(proxy_addr,url):
    proxy = urllib.request.ProxyBasicAuthHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(url).read().decode('utf-8')
    return data

proxy_addr = '61.163.39.70:9999'
data = use_proxy(proxy_addr,'http://www.baidu.com')
print(len(data))