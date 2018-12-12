# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-11
# file: 关闭实例的dict
# description:

import sys

class Player:
    def __init__(self,id,name,age,status=0,level=1):
        self.id = id
        self.name = name
        self.age = age
        self.status =status
        self.level = level

class Player2():
    __slots__ = ('id','name','age','status')

    def __init__(self,id, name, age, status=0, level=1):
        self.id = id
        self.name = name
        self.age = age
        self.status = status
        # self.level = level

p1 = Player(1,'jim',15) # ==> 56
p2 = Player2(2,'john',11) # ==> 80

print(p2.__slots__)
# print(p2.__dict__) # 没有dict属性


print('p1占用空间的字节大小为：',sys.getsizeof(p1))
print('p2占用空间的字节大小为：',sys.getsizeof(p2))

print('p1和p2的差集：',set(dir(p1))-set(dir(p2)))
