# -*- coding: utf-8 -*-
# @Time:2021/3/6 6:23 下午
# @Author:lvlv
# @File:thread_test_3st.py

import logging
import threading
from time import ctime, sleep
# 使用threading模块，免去加锁的麻烦

# 设置日志级别为info
logging.basicConfig(level = logging.INFO)
# 线程执行时间列表
loops = [4,2]

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
        t = threading.Thread(target=loop,args=(i,sectime))
        threads.append(t)
    for i in range(len(loops)):
        threads[i].start() # 启动子线程
    for i in range(len(loops)):
        threads[i].join() # 等待子线程执行完毕释放锁
    logging.info("start end at " + ctime())

if __name__ == '__main__':
    main()

