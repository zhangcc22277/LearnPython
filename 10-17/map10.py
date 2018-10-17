#coding =utf-8

#python 提供的sum（）函数可以接受list并求和，请编写一个prod（）函数，可以接受一个
#list并用reduce（）求积
from functools import reduce
def prod(L):
    def mul(x,y)

        return x*y
    return reduce(mul,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')