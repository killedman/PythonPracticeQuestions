#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-23
# 第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）,
# 请将上述内容写到 numbers.xls

# 步骤1： 读取numbers.txt
# 步骤2： 创建excel对象

from openpyxl import Workbook
import json

def read_txt_file():
    with open('./numbers.txt','r',encoding='utf-8-sig') as file:
        load_dict = json.load(file)
    return load_dict

def create_excel_file(numbers):
    wb = Workbook()
    sheet = wb.active
    sheet.title = "numbers"
    i = 0
    for number in numbers:
        i = i + 1
        sheet["A%d" %i].value,sheet["B%d" %i].value,sheet["C%d" %i].value = number
    wb.save('./numbers.xlsx')

if __name__ == "__main__":
    numbers = read_txt_file()
    create_excel_file(numbers)