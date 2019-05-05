# -*- coding=utf-8 -*-

# assert断言影响性能，禁止启用python -O name.py,最好调试阶段使用
x = 1
y = 1
assert x == y, "not equals"


# lazy evaluation
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


from itertools import islice

print '第10章结果{info}'.format(info=list(islice(fib(), 5)))

# 枚举值　https://www.cnblogs.com/ucos/p/5896861.html
from enum import Enum, unique


@unique
class Color(Enum):
    red = 1
    yellow = 2

# 不建议使用type来判断，基于内建类型拓展的用户自定义类型，type函数并不能准确返回结果
