# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-12
# file: 保存被修饰函数的元数据
# description:

# =========== 方式1. 将原函数的所有需要的属性都付给被包裹的函数   ============================
def log(level="low"):
    def deco(func):
        def wrapper(*args,**kwargs):
            print("log was in...")
            if level == "low":
                print("detailes was needed")
            return func(*args,**kwargs)
        wrapper.__name__ = func.__name__
        wrapper.__dict__ = func.__dict__
        return wrapper
    return deco

@log()
def myFunc():
    '''I am myFunc...'''
    print("myFunc was called")

print(myFunc.__name__)
myFunc()
print(myFunc.__name__)

# 缺点是：需要大量复制的操作

# =========== 方式2. 使用functools的wrapper，update_wrapper  ============================
from functools import wraps,update_wrapper

def log(level="low"):
    def deco(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print("log was in...")
            if level == "low":
                print("detailes was needed")
            return func(*args,**kwargs)
        update_wrapper(wrapper, func, ('__name__','__doc__'), ('__dict__',))
        return wrapper
    return deco

@log()
def myFunc():
    print("myFunc was called")

print(myFunc.__name__)
myFunc()
print(myFunc.__name__)

