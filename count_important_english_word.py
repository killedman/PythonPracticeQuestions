#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-22
# 统计存储英文日记目录中每篇日记中最重要的词（出现频率最高的词）
# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
# 假设内容都是英文，请统计出你认为每篇日记最重要的词。

import sys
import os

#读取文件并以空格符作为分隔符存储在列表中
def read_file(artical):
    # 以二进制方式打开文件，解决UnicodeDecodeError: 
    # 'gbk' codec can't decode byte 0xa2 in position 600: 
    # illegal multibyte sequence这样的报错
    with open(artical, 'rb') as file:
        content = file.read().decode('utf-8')
    return content.split()

def count_word():
    if len(sys.argv) > 1:
            if sys.argv[1] and os.path.exists(sys.argv[1]):
                for artical in os.listdir(sys.argv[1]):
                    # 文章原始单词列表
                    source_words = []
                    # 文章每个单词出现频率统计字典
                    count_of_words = {}
                    artical = os.path.join(sys.argv[1],artical)
                    source_words = read_file(artical)
                    for word in source_words:
                        if count_of_words.get(word):
                            count_of_words[word] += 1
                        else:
                            count_of_words[word] = 1
                    # 按照word出现的频率排序
                    sorted_list = sorted(count_of_words.items(), \
                        key=lambda d: d[1], reverse=True)
                    print(sorted_list[0])
            else:
                print('请检查输入的目录名及路径是否正确')
    else:
        print('请输入要处理的目录名,E.g: python count_important_english_word.py d:\\words_test')    


if __name__ == "__main__":
    count_word()