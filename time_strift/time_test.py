# -*- coding: utf-8 -*-
# @Time:2021/2/6 4:53 下午
# @Author:lvlv TYC0811
# @File:time_test.py

import time

#获取国际标准时间
print(time.asctime())
#获取当前时间戳
print(time.time())
#获取当前时间元祖
time_tuple = time.localtime()
#将时间输出至自定义格式
print(time.strftime('%Y-%m-%d %H:%M:%S', time_tuple))