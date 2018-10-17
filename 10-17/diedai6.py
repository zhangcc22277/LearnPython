#coding =utf-8
#请使用迭代查找一个list中最小和最大值，并返回一个tuple

def findMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        Max = L[0];
        Min = L[0];
        for value in L:
            if value > Max:
                Max = value
        for value in L:
            if value < Min:
                Min = value
        return (Min,Max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')