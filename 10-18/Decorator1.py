#coding =utf-8

#请设计一个decorator，它可以作用于任何函数上，并打印盖函数的执行时间

import time,functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        fn(*args, **kw)
        end = time.time()
        print('%s execute in %s ms' % (fn.__name__, end-start))
        return fn(*args, **kw)
    return wrapper
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


f = fast(11, 22)
print(f)

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')