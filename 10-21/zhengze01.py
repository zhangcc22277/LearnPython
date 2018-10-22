#coding =utf-8
#获取title标签的内容
import  re
import urllib.request

url = "http://www.baidu.com/"
pattern = r'<title>(.*?)</title>'

content = urllib.request.urlopen(url).read().decode('utf-8')
pat = re.compile(pattern).findall(content)
# pat = pat.decode('utf-8')
print(pat[0])
#百度一下，你就知道