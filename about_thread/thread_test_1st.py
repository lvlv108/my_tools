# -*- coding: utf-8 -*-
# @Time:2021/3/4 2:59 下午
# @Author:lvlv TYC0811
# @File:thread_test_1st.py
import _thread
import logging
from time import ctime, sleep

#设置日志级别
logging.basicConfig(level = logging.INFO)

#定义第一个子线程
def loop0():
    logging.info("start loop0 at " + ctime())
    sleep(4)
    logging.info("start loop0 at " + ctime())
#定义第二个子线程
def loop1():
    logging.info("start loop1 at " + ctime())
    sleep(2)
    logging.info("start loop1 at " + ctime())
#定义主线程
def main():
    logging.info("start all at " + ctime())
    _thread.start_new_thread(loop0,())  #_thread 是threading的低级用法
    _thread.start_new_thread(loop1,())
    sleep(6)  #_thread的缺点之一，若不给主线程设置等待时间，则主线程结束，子线程自动被kill
    logging.info("start all at " + ctime())

if __name__ == '__main__':
    main()
