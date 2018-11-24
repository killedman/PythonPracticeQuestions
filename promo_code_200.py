#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-21
# description： 生成200个促销码
import string
import random

#产生促销码数据源
source_list = []
# 促销码位数
number = 10
# 存储200个促销码的list
promo_code_list = []

def gen_promo_code():
    # 包含大小写的26个字母、0-9的列表
    source_list = list(string.ascii_letters+string.digits)
    # 随机返回number位的字符串
    return ''.join(random.sample(source_list,number))

# 生成200个促销码
for i in range(200):
    promo_code_list.append(gen_promo_code())

print(promo_code_list)