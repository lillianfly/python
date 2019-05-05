# -*- coding=utf-8 -*-

# 1
# 快排
def quicksort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    key = array.pop()
    for data in array:
        if data <= key:
            less.append(data)
        else:
            greater.append(data)
    return quicksort(less) + [key] + quicksort(greater)


# 交换
a = 1
b = 2
a, b = b, a

# 打印
print('hello %s!' % ('Tom',))
print('hello %(name)s' % {'name': 'Tom!'})
print('{great} from {lag}'.format(great='Hello world', lag='Python') ) # 最建议的语法

# 3
# 三元运算符
x = 0
y = -2
print(x if x < y else y)

# swith
n = 0
if n == 0:
    print (n)
elif n == 1:
    print (n + 1)
else:
    print (n + 2)


def f(x):
    return {
        0: n,
        1: n + 1
    }.get(x, x + 2)


# 7　常量放在一起const.py方便管理
import const

print ('{lession}值为{number}'.format(lession='第7课',number=const.FIRST*5))
