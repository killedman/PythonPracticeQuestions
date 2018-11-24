#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-18
# 产生的200个促销码
# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中

import string
import random
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 促销码位数
number = 10
# 存储生成促销码的列表
promo_code_list = []

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'
    # 表的结构
    id = Column(String(20), primary_key = True)
    name = Column(String(20))

# 定义promo_code对象
class promo_code(Base):
    # 表的名字
    __tablename__ = 'promo_code'
    # 表的结构
    id = Column(Integer, primary_key = True)
    code = Column(String(20))

# 用来随机生成一个字符串
def gene_text(number):
    source = list(string.ascii_letters)
    for index in range(0, 10):
        source.append(str(index))
    return ''.join(random.sample(source, number))

if __name__ == '__main__':
    # 初始数据库连接
    engine = create_engine('mysql + pymysql://%s:%s@%s:3306/%s?charset=utf8'\
     %('root', 'root', '127.0.0.1', 'test'))

    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)
    for i in range(200):
        promo_string = gene_text(number)
        promo_code_list.append(promo_string)
    
    # 创建session对象
    session = DBSession()
    for i in range(len(promo_code_list)):
        new_user = promo_code(id=1,code=promo_code_list[i])
        # 添加到session
        session.add(new_user)
        # 提交即保存到数据库
        session.commit()
    # 关闭session
    session.close()