# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-12
# file: 函数装饰器
# description:

import logging

# =======       改进方式1.直接在原函数上添加          =================
def foo():

    print('foo function')
    logging.info('foo is running') # 增加打印log功能


def bar():
    print('bar function')
    logging.info('bar is running')  # 增加打印log功能


# =======    改进方式2. 重新定义新的函数，包裹要添加的项   =================
def use_logging(func):
    print(type(func))
    logging.info('%s is running' %func.__name__)
    func()
use_logging(foo)
# 这种方式破坏了原有的代码的逻辑结构，使得原先的调用是foo()变成use_logging(foo)

# ========   改进方式3. 装饰器返回包裹的函数       ==============
def use_logging(func):

    # 使用函数闭包，返回包装后的原函数，这样在调用原函数的时候会先调用闭包内的内容
    def wrapper(*args,**kwargs):
        logging.info('%s is running' %func.__name__)
        return func(*args,**kwargs)

    return wrapper

foo = use_logging(foo)
foo()
# 这种方式使得函数在进入和退出的时候像是一个横切面，也被称为面向切面编程


# ========   改进方式4. 装饰器符号方式    ==============
def use_logging(func):

    # 使用函数闭包，返回包装后的原函数，这样在调用原函数的时候会先调用闭包内的内容
    def wrapper(*args,**kwargs):
        logging.info('%s is running' %func.__name__)
        return func(*args,**kwargs)

    return wrapper

@use_logging
def foo():
    print('foo function')
    logging.info('foo is running') # 增加打印log功能
# 这种方式使用装饰器符号，省去代码foo=use_logging(foo)
foo()


# ===  带参数的函数装饰器 ===================
import logging

# =======       改进方式1.直接在原函数上添加          =================
def foo():

    print('foo function')
    logging.info('foo is running') # 增加打印log功能


def bar():
    print('bar function')
    logging.info('bar is running')  # 增加打印log功能


# =======    改进方式2. 重新定义新的函数，包裹要添加的项   =================
def use_logging(func):
    print(type(func))
    logging.info('%s is running' %func.__name__)
    func()
use_logging(foo)
# 这种方式破坏了原有的代码的逻辑结构，使得原先的调用是foo()变成use_logging(foo)

# ========   改进方式3. 装饰器返回包裹的函数       ==============
def use_logging(func):

    # 使用函数闭包，返回包装后的原函数，这样在调用原函数的时候会先调用闭包内的内容
    def wrapper(*args,**kwargs):
        logging.info('%s is running' %func.__name__)
        return func(*args,**kwargs)

    return wrapper

foo = use_logging(foo)
foo()
# 这种方式使得函数在进入和退出的时候像是一个横切面，也被称为面向切面编程


# ========   改进方式4. 装饰器符号方式    ==============
# 多增加一层函数接收参数
def use_logging(level):

    def decorator(func):

        # 使用函数闭包，返回包装后的原函数，这样在调用原函数的时候会先调用闭包内的内容
        def wrapper(*args,**kwargs):
            logging.info('%s is running' %func.__name__)
            return func(*args,**kwargs)
        return wrapper

    return decorator

@use_logging
def foo():
    print('foo function')
    logging.info('foo is running') # 增加打印log功能
# 这种方式使用装饰器符号，省去代码foo=use_logging(foo)
foo()


