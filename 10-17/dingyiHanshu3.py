#coding =utf-8

#请定义一个函数quadratic（a，b，c），接收3个参数，返回一元二次方程ax2+bx+c=0的两个解。

import math
def quadratic(a,b,c):
    delta = b*b-4*a*c
    if a==0:
        x0 =-c/b
        return x0
    #此时不是一元二次方程
    elif delta==0:
        x1=x2 =-b/(2*a)
        return x1,x2
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        return x1,x2
a=int(input("a:"))
b=int(input("B:"))
c=int(input("C;"))
print(quadratic(a,b,c))

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')