#coding =utf-8
#一个get（）的简单数据库

#再这里插入代码清单4-1中的数据库（字典people）

labels={
    "phone":"phone number",
    "addr":"addr"
}
name =input("name:")

#要查找的电话号码还是地址？
request = input("phone number(p) or address (a)")

#使用正确的键
key =request  #如果request既不是‘p’也不是‘a’
if request =="p":key="phone"
if request =="a":key ="addr"

#使用get提供默认值
person = labels.get(name,{})
label = labels.get(key,key)
result = person.get(key,"not available")

print("{}'s {} is {}.".format(name,label,result))