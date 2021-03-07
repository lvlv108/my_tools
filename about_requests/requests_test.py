# -*- coding: utf-8 -*-
# @Time:2021/3/6 10:05 下午
# @Author:lvlv
# @File:requests_test.py
import requests

def requests_test():
    # res = requests.get('http://www.baidu.com')
    # print(res.status_code,res.text)

    res = requests.post("http://httpbin.org/post",data = {"key":"value"})
    print(res.text)


if __name__ == '__main__':
    requests_test()