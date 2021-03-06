# -*- coding: utf-8 -*-
# @Time:2021/3/5 9:15 上午
# @Author:lvlv
# @File:thread_test_2st.py
import _thread
import logging
from time import ctime, sleep

# 设置日志级别为info
logging.basicConfig(level = logging.INFO)
# 线程执行时间列表
loops = [4,2]

def loop(nloop,sectime,lock):
    '''
    定义子线程执行方法
    :param nloop: 子线程序号
    :param sectime: 单个子线程执行的时间
    :param lock: 线程锁
    :return:
    '''
    logging.info("start loo " + str(nloop) + " at " + ctime())
    sleep(sectime)
    logging.info("end loop"+ str(nloop) + " at " + ctime())
    lock.release() # 释放锁

def main():
    '''
    定义执行主线程
    :return:
    '''
    logging.info("start all at " + ctime())
    lock = []
    for i in range(len(loops)):
        nlock = _thread.allocate_lock() # 获取锁
        nlock.acquire() # 将上一步获得到的锁锁上
        lock.append(nlock)
    for i in range(len(loops)):
        # 这里不能与上一步加锁合并，因为获取锁，是需要时间的，有可能在获取第二个锁的时候，第一个线程已经执行完毕了，
        # 释放了锁，这时候就会导致主线程停止等待，第二个线程无法执行，直接被kill
        sectime = loops[i]
        _thread.start_new_thread(loop, (i,sectime,lock[i]))
    for i in range(len(loops)):
        # 用来判断是否还有锁上的锁，若有则无限循环直至最后一个子线程执行完释放了最后一个锁
        while lock[i].locked():
            pass
    logging.info("start end at " + ctime())

if __name__ == '__main__':
    main()

