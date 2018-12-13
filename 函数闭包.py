# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-12
# file: 函数闭包
# description:

def adder(x):
    def wrapper(y):
        return x + y
    return wrapper

adder5 = adder(5)

adder6 = adder5(10)
print(adder6)
# ==> 15,因为函数最开始封装了x=5


# 输出 11
adder7 = adder5(6)
print(adder7)
# ==> 11，因为函数最开始封装了x=5