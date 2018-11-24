#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-22
# 将产生的200个促销码存储在redis数据库中

import redis
import string
from gene_200_prome_code import gene_text

# 促销码位
bit = 10
# 促销码个数
number = 200

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
for i in range(number):
    r.sadd('200_promo_code',gene_text(bit))
print(r.smembers('200_promo_code'))