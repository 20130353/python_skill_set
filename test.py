# # -*- coding: utf-8 -*-
# # author: sunmengxin
# # time: 18-12-13
# # file: test
# # description:
#
# class Myclass:
#     def __init__(self, a):
#         self.a = a
#
#     def printa(self):
#         print(self.a)
#
#
# print(id(3))
# mclass = Myclass(3)
# mclass.printa()
# print(id(mclass.a))
#
# print('-----------------')
#
# print(id(1000))
# mclass.a = 1000
# mclass.printa()
# print(id(mclass.a))
#
# print('-----------------')
# a = [1,2,3]
# print(id(a))
# mclass.a = a
# mclass.printa()
# print(id(mclass.a))
#
# print('-----------------')
#
# mclass.a[1] = 4
# mclass.printa()
# print(id(mclass.a))
# print(a)
#
# print('-----------------')
# a[1] = 5
# mclass.printa()
# print(id(mclass.a))
# print(a)

class C1(object):
    a = 100
    b = 100
    c = 1000
    d = 1000


class C2(object):
    a = 100
    b = 1000


c1 = C1()
c2 = C2()
print(id(c1.c))  # == >
print(id(c2.b))  # == >

a = 1000
print(id(a))  # == >
c1.c = a
c2.b = a
print(id(c1.c))  # == >
print(id(c2.b))  # == >
