#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-23
# 第 0008 题： 一个HTML文件，找出里面的正文

from html.parser import HTMLParser

class  MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print(data)

parser = MyHTMLParser()

with open('./parser.html','r',encoding='utf8') as file:
    parser.feed(file.read())
