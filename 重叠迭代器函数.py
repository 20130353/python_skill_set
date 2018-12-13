# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-12
# file: 重叠迭代器函数
# description:

from time import ctime


def deco1(func):
    def decorator1(*args, **kwargs):
        print('decorator1 print')
        print('[%s]  %s() is called' % (ctime(), func.__name__))
        return func(*args, **kwargs)

    return decorator1


def deco2(func):
    def decorator2(*args, **kwargs):
        print('decorator2 print')
        print('[%s]  %s() is called' % (ctime(), func.__name__))
        return func(*args, **kwargs)

    return decorator2


@deco2
@deco1
def foo():
    print('Hello, Python')
foo()

# decorator2 print
# [Wed Dec 12 15:32:19 2018]  decorator1() is called
# decorator1 print
# [Wed Dec 12 15:32:19 2018]  foo() is called
# Hello, Python

