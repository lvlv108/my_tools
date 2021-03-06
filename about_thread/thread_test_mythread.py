# -*- coding: utf-8 -*-
# @Time:2021/3/6 8:15 下午
# @Author:lvlv
# @File:thread_test_mythread.py


import logging
import threading
from time import ctime, sleep
# 实现thread类的二次开发

# 设置日志级别为info
logging.basicConfig(level = logging.INFO)
# 线程执行时间列表
loops = [4,2]
class myThread(threading.Thread):
    def __init__(self,func,args,name = ''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        self.func(*self.args)

def loop(nloop,sectime):
    '''
    定义子线程执行方法
    :param nloop: 子线程序号
    :param sectime: 单个子线程执行的时间
    :param lock: 线程锁
    :return:
    '''
    logging.info("start loop" + str(nloop) + " at " + ctime())
    sleep(sectime)
    logging.info("end loop"+ str(nloop) + " at " + ctime())

def main():
    '''
    定义执行主线程
    :return:
    '''
    logging.info("start all at " + ctime())
    threads = []
    for i in range(len(loops)):
        sectime = loops[i]
        t = myThread(loop,(i,sectime),loop.__name__)
        threads.append(t)
    for i in range(len(loops)):
        threads[i].start() # 启动子线程
    for i in range(len(loops)):
        threads[i].join() # 等待子线程执行完毕释放锁
    logging.info("start end at " + ctime())

if __name__ == '__main__':
    main()

"""
原语：多线程的核心就是多个线程可以访问同一个数据，但是一定会造成数据的错误，原语操作包括几个子概念：
     锁：（_thread中的锁并非真正意义上的锁）原语用锁解决了数据的互斥访问，数据可以只允许一个线程进行访问
     信号量：比锁更加灵活，锁可能就是一个true或false，信号量可以设置0，1，2，3等各种值
     这些都属于原语操作
     
"""
