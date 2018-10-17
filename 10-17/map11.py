#coding =utf-8
#利用map和reduce编写一个str2float函数，把‘123.456’转换成浮点123.456!!!!!!!!!!!!!!!!!!!!!!!

from  functools import  reduce
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    # 取得小数点的位置
    p = s.index('.')
    # 把小数点前后分成2个字符串
    s1 = s[0:p]
    s2 = s[(p + 1):]

    # 定义2个函数用于把字符串变为int
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    # 第二个字符串有多少位,它的int就乘以10的-多少次方还原为小数
    return reduce(fn, map(char2num, s1)) + reduce(fn, map(char2num, s2)) * (10 ** (0 - len(s2)))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')