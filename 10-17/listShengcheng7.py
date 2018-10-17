#coding =utf-8

#请修改列表生成式，通过添加if语句保证列表声称是能正确的执行
L1 =['hello','World',18,'apple',None]
L2 =[a.lower() for a in L1 if isinstance(a,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')