#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-23
# 第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
# 请将上述内容写到 student.xls 文件中

from openpyxl import Workbook
import json

def read_txt_file():
    with open('./student.txt','r',encoding='utf-8-sig') as file:
        load_dict = json.load(file)
    return load_dict

def create_excel_file(students):
    wb = Workbook()
    sheet = wb.active
    sheet.title = "student"
    i = 0
    for student in students:
        i = i + 1
        sheet["A%d" %i].value = student
        sheet["B%d" %i].value,sheet["C%d" %i].value, sheet["D%d" %i].value, \
            sheet["E%d" %i].value = students.get(student)
    wb.save('./students.xlsx')

if __name__ == "__main__":
    student_dict = read_txt_file()
    create_excel_file(student_dict) 