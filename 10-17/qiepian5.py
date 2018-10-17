#coding =utf-8
#利用求片操作，实现一个trim（），去除字符串是首尾的空格，注意不要调用str的strip（）方法：
def trim(s):

    while s == '':
        return s
    while s[0] == ' ':
        s = s[1:]
        if s == '':
            return s
    while s[-1] == ' ':
        s = s[:-2]
    return s
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')