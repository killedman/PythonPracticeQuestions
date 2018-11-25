#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-23
# 当用户输入敏感词语时，则打印出Freedom，否则打印Human Rights
# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

def read_senstive_word():
    words = []
    with open('./filtered_words.txt', 'r', encoding='utf8') as file:
        content = file.readlines()
        for line in content:
            # 去除开头的\ufeff字符
            line = line.replace('\ufeff', '')
            # 去除换行符
            line = line.strip()
            words.append(line)
    return words

def check_input_word(checked_word, sensitive_word):
    if checked_word in sensitive_word:
        print('Freedom')
    else:
        print('Human Rights')


def input_word(checked_word, sensitive_word):
    while checked_word:
        check_input_word(checked_word, sensitive_word)
        checked_word = input('please input word: ')

if __name__ == '__main__':
    print('begin input word...')
    print('attention: Hit the Enter key will quit this program.')
    sensitive_word = read_senstive_word()
    checked_word = input('please input word: ')
    input_word(checked_word, sensitive_word)