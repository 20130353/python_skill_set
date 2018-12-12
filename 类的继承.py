# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-11
# file: 类的继承
# description:

import abc
class Person(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'

    def talk(self):
        print("person is talking....")

    def walk(self): # 抽象函数，每个如果子类使用这个函数但是没有实现就会出错,错误是在调用函数的时候发生
        raise NotImplementedError

    @abc.abstractmethod
    def eat(self): # 抽象函数，如果子类定义的时候没有实现这个函数就会出错。错误实在实例化的时候发生
        return



class Chinese(Person):

    def __init__(self, name, age, language):
        Person.__init__(self, name, age) # 先调用父类的init函数，之后在调用子类的函数
        self.language = language

    def talk(self):  # 子类的重构方法，直接写和父类一样的名称即可
        print('%s is speaking chinese' % self.name)


c = Chinese('bigberg', 22, 'Chinese')
c.talk()
c.eat()
c.walk()

#
import abc

# 定义抽象类
class Sheep(object,metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_size(self):
        return


class sheepson(Sheep):
    def __init__(self):
        print('sheepson.__init__ is called!')


s1 = Sheep()  # 报错，不能实例化抽象类
s2 = sheepson()#报错，不能实例化抽象类