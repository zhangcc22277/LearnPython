#coding =utf-8
#获取tr/td标签间的内容

import re
import urllib.request
#获取《》tr之间的内容
url = "http://www.baidu.com"
pat = r'<tr>(.*?)</tr>'
content = urllib.request.urlopen(url).read().decode('utf-8')
pattern = re.compile(pat).findall(content,re.S|re.M)
for m in pattern:
    print(m)
#获取th之间的内容

for m in pattern:
    pat_th = r'<th>(.*?)</th>'
    m_th = re.compile(pat_th).findall(m,re.S|re.M)
    for t in m_th:
        print(t)

#直接获取th之间的内容

pat_td = r'<td>(.*?)<td></td>(.*?)</td>'
t_td = re.compile(pat_td).findall(content,re.S|re.M)
for h in t_td:
    print(h[0],h[1])
#结果类似于：
# < th > 学号 < / th > < th > 姓名 < / th >
# < td > 1001 < / td > < td > 杨秀璋 < / td >
# < td > 1002 < / td > < td > 严娜 < / td >
#
# 学号
# 姓名
#
# 1001
# 杨秀璋
