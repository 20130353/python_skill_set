# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-11
# file: 修改类属性
# description:


class IntTuple(tuple):
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        # print self
        tuple.__init__(iterable)
        # super(IntTuple, self).__init__(iterable) # 不知道这种方式为什么不可以调用父类的init函数

t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])