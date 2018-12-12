# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-11
# file: 属性管理器
# description:

class Student(object):

    @property
    def score(self): #相当于是getter方法
        print('getter')
        return self._score

    @score.setter
    def score(self, value):
        print('setter')
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 100
print(s.score)
#
# setter
# getter
# 100