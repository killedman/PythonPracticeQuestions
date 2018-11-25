#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-23
# 第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
# 请将上述内容写到 city.xls 文件中

# 步骤1： 读取city.txt中的数据
# 步骤2： 创建excel对象

from openpyxl import Workbook
import json

def read_txt_file():
    with open('./city.txt','r',encoding='utf-8-sig') as file:
        load_dict = json.load(file)
    return load_dict

def create_excel_file(citys):
    wb = Workbook()
    sheet = wb.active
    sheet.title = "citys"
    i = 0
    for city in citys:
        i = i + 1
        sheet["A%d" %i].value = city
        sheet["B%d" %i].value = citys.get(city)
    wb.save('./citys.xlsx')

if __name__ == "__main__":
    citys = read_txt_file()
    create_excel_file(citys)
    