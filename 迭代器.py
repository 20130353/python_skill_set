# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-11
# file: 迭代器
# description:

it = iter([1,2,3,4])
print(next(it))
print(it.__next__())
print(it.__next__())
print(it.__next__())