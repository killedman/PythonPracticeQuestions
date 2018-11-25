#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-22
# 统计写的代码行数，包括注释和空行，但要单独列出来
# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
# 包括空行和注释，但是要分别列出来

import sys
import os

def read_code_file(codefile):
    comment_lines = 0
    code_lines = 0
    space_lines = 0
    # 二进制方式打开文件，使用utf-8解码解决UnicodeDecodeError报错
    with open(codefile, 'rb') as file:
        for line in file.read().decode('utf-8'):
            # 统计注释行
            if line.startswith('#'):
                comment_lines += 1
            # 统计空行
            elif not line.strip():
                space_lines += 1
            # 统计代码行
            else:
                code_lines += 1
    return (comment_lines, code_lines, space_lines)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] and os.path.exists(sys.argv[1]):
            for codefile in os.listdir(sys.argv[1]):
                if os.path.splitext(codefile)[1] == '.py':
                    codefile = os.path.join(sys.argv[1], codefile)
                    comment_lines, code_lines, space_lines = read_code_file(codefile)
                    print('代码文件%s统计结果： 注释行数 %d, 代码行数 %d, 空行数 %d'\
                         %(codefile, comment_lines,code_lines,space_lines))
        else:
            print('请检查输入的目录名及路径是否正确')
    else:
        print('请输入要处理的目录名，E.g: python count_code_lines.py d:\\codes_test')