# -*- coding: utf-8 -*-
# @Time:2021/3/7 7:05 下午
# @Author:lvlv
# @File:yaml_test.py
import yaml

# 将yaml格式转化为列表

# print(yaml.load("""
#  - Hesperiidae
#  - Papilionidae
#  - Apatelodidae
#  - Epiplemidae
#  """,Loader= yaml.FullLoader))

# 将yaml格式转化为字典

# print(yaml.load("""
# a: 1
# """, Loader=yaml.FullLoader))

# 从yaml文件读取数据并转化为python数据类型

# print(yaml.load(open("yaml_info.yml"), Loader=yaml.FullLoader))

# 将python数据类型转换为yaml文件流

# print(yaml.dump({"a" : [1,2]}))

# 将python数据类型转换为yaml文件流并输出到文件
with open("yaml_out.yml","w") as f:
    yaml.dump({"a" : [1,2]},stream = f)



