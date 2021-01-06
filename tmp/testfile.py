# -*- coding:utf-8 -*-

import re

a = "not 404 found 张三 99 深圳"
alist = a.split(" ")
res = re.findall('\d+|[a-zA-Z]+', a)
print(list(res))

a = (1,)
print(type(a))
