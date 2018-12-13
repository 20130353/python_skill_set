# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-12
# file: 线程
# description:

from time import ctime, sleep
# =============     方式1. 基本的单线程执行任务            ==================

def music(names):
    for i in range(len(names)):
        print('at time: %s, i am listening music %s' % (ctime(), names[i]))
        sleep(1)
    return


def movie(names):
    for i in range(len(names)):
        print('at time: %s, i am watching movie %s' % (ctime(), names[i]))
        sleep(5)


if __name__ == '__main__':
    music(('光年之外', '青花瓷'))
    movie(('暗战', '熔炉'))
    print('at time %s, all is over' % ctime())



# =============     方式2. 多线程执行任务            ==================
import threading
from itertools import chain

def music(name):
    print('at time: %s, music %s start' % (ctime(), name))
    sleep(1)
    print('at time: %s, music %s end' % (ctime(), name))
    return


def movie(name):
    print('at time: %s, movie %s start' % (ctime(), name))
    sleep(5)
    print('at time: %s, movie %s end' % (ctime(), name))


if __name__ == '__main__':

    threads = []
    for inx, x in enumerate(chain(('光年之外', '青花瓷') + ('暗战', '熔炉'))):
        if inx < 2:
            threads.append(threading.Thread(target=music, args=(x,))) #传递参数需要传递元组的形式，否则会把一个元素拆成多个元素
        else:
            threads.append(threading.Thread(target=movie, args=(x,)))

    for t in threads:
        t.setDaemon(True)  # 设置为守护线程，如果不设置为守护线程会被无限挂起
        t.start()

    # 这个程序会在主线程执行完结束后直接结束子线程
    print('at time %s, all is over' % ctime())


# =============     方式3. 多线程改进，使主线程等待子线程结束之后再结束      ==================
import threading
from itertools import chain

def music(name):
    print('at time: %s, music %s start' % (ctime(), name))
    sleep(1)
    print('at time: %s, music %s end' % (ctime(), name))
    return


def movie(name):
    print('at time: %s, movie %s start' % (ctime(), name))
    sleep(5)
    print('at time: %s, movie %s end' % (ctime(), name))


if __name__ == '__main__':

    threads = []
    for inx, x in enumerate(chain(('光年之外', '青花瓷') + ('暗战', '熔炉'))):
        if inx < 2:
            threads.append(threading.Thread(target=music, args=(x,))) #传递参数需要传递元组的形式，否则会把一个元素拆成多个元素
        else:
            threads.append(threading.Thread(target=movie, args=(x,)))

    for t in threads:
        t.setDaemon(True)  # 设置为守护线程，如果不设置为守护线程会被无限挂起
        t.start()

    t.join() # 使子线程完成之前，这个父线程将会被一直阻塞

    # 这个程序会在主线程执行完结束后直接结束子线程
    print('at time %s, all is over' % ctime())
