# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-11
# file: 是实现迭代器和可迭代对象
# description:

# - 实际问题：某软件需求，从网络抓取各个城市的气温信息，并一次显示，
# 如果一次抓取所有城市的信息，那么显示第一个城市的信息时会存在长期的时延问题。
# 我们希望能使用“用时访问”的策略，并且把所有城市的气温封装到一个对象中，可以用for循环来迭代，如何解决问题？
# 解决方案：实习一个迭代器和一个可迭代对象

import requests
from collections import Iterable, Iterator


# 迭代器是针对城市的，所有要有一个城市列表
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities  # 城市列表
        self.index = 0  # 访问的位置记录

    def get_wather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

    def __next__(self):
        print('迭代器 next')
        if self.index == len(self.cities):
            raise StopIteration

        city = self.cities[self.index]
        self.index += 1
        return self.get_wather(city)


class WeatherIterable(Iterable):

    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        print('可迭代对象 iter')
        # 可迭代对象遍历的时候调用的迭代器的next函数。
        # 返回的是一个迭代器对象
        return WeatherIterator(self.cities)


class WeatherGenerator():

    def __init__(self, cities):
        self.cities = cities

    def get_wather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

    def __iter__(self):
        for x in self.cities:
            yield self.get_wather(x)


# for x in WeatherIterable(['北京', '天津', '上海']):
#     print(x)
# ==>
# 可迭代对象 iter
# 迭代器 next
# 北京: 低温 -10℃, 高温 -1℃
# 迭代器 next
# 天津: 低温 -5℃, 高温 1℃
# 迭代器 next
# 上海: 低温 3℃, 高温 9℃
# 迭代器 next


x = iter(WeatherGenerator(['北京', '天津', '上海']))
print(list(x))
# ==>
# 可迭代对象 iter
# 迭代器 next
# 迭代器 next
# 迭代器 next
# 迭代器 next
# ['北京: 低温 -10℃, 高温 -1℃', '天津: 低温 -5℃, 高温 1℃', '上海: 低温 3℃, 高温 9℃']
