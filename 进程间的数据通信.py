# -*- coding: utf-8 -*-
# author: sunmengxin
# time: 18-12-12
# file: 进程间的数据通信
# description:

# 下载电影之后才能看电影，而且下载好电影之后需要通知看电影的进程
#

from time import ctime, sleep
# =============     方式1. 基本的单线程执行任务            ==================
from queue import Queue
import threading

def download(data_q):
    while True:
        data = ctime()
        print('put in ', data)
        data_q.put(data)



def consume(data_q):
    while True:
        data = data_q.get()
        print('consume ', data)


if __name__ == '__main__':
    q = Queue()
    threads = []

    for _ in range(2):
        threads.append(threading.Thread(target=download, args=(q,)))
        threads.append(threading.Thread(target=consume, args=(q,)))
    for t in threads:
        t.setDaemon(True)
        t.start()
