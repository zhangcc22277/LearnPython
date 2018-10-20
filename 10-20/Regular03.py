#coding =utf-8
import re

#compile 匹配相应的对象
#该函数根据包含正则表达式的字符串创建模式对象，返回一个pattern对象
pattern = re.compile()
#match方法
pattern.match()#从起始位置开始往后查找，返回第一个符合规则的，只匹配一次
pattern.search()#从任何位置开开始，往后查找，返回第一个符合规则的，只匹配一次
pattern.findall()#所有的全部匹配，返回列表
pattern.split()#分割字符串，返回列表
pattern.sub()#替换

