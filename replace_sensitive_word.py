#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-23
# 第 0012 题： 敏感词文本文件 filtered_words.txt,当用户输入敏感词语，则用 星号 * 替换，
# 例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

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

def replace_input_word(checked_word, sensitive_word):
    for word in sensitive_word:
        if word in checked_word:
            checked_word = checked_word.replace(word, '*')
    print(checked_word)

def input_word(checked_word, sensitive_word):
    while checked_word:
        replace_input_word(checked_word, sensitive_word)
        checked_word = input('please input word: ')

if __name__ == '__main__':
    print('begin input word...')
    print('attention: Hit the Enter key will quit this program.')
    sensitive_word = read_senstive_word()
    checked_word = input('please input word: ')
    input_word(checked_word, sensitive_word)