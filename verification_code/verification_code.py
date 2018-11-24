#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-11-24
# 第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片

import random
import string
from PIL import Image,ImageFont,ImageDraw,ImageFilter

# 图片存储路径
SavePath = 'd:\\test_yzm.png'
#字体路径
font_path = '.\\arial.ttf'
#生成几位验证码
number = 4
#生成验证码的图片宽度和高度
size = (100, 30)
#验证码背景，默认为白色
bgcolor = (255, 255, 255)
#字体颜色，默认为蓝色
fontcolor = (0, 0, 255)
# 干扰线颜色，默认为红色
linecolor = (255, 0, 0)
#是否要加入干扰线
draw_line = True
# 加入干扰线条数的上下限
line_number = (2, 5)

# 用来随机生成一个字符串
def gene_text():
    source = list(string.ascii_letters)
    for index in range(0, 10):
        source.append(str(index))
    return ''.join(random.sample(source, number))

# 生成干扰线
def gene_line(draw, width, height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill = linecolor)

# 生成验证码
def gene_code():
    width, height = size
    # 创建图片
    image = Image.new('RGBA', (width, height), bgcolor)
    # 验证码的字体和字体大小
    font = ImageFont.truetype(font_path, 25)
    # 创建画笔
    draw = ImageDraw.Draw(image)
    text = gene_text()
    font_width, font_height = font.getsize(text)
    # 填充字符串
    draw.text(((width - font_width) / number, 
            (height - font_height) / number),
            text, font = font, fill = fontcolor)
    if draw_line:
        gene_line(draw, width, height)
    # 创建扭曲
    image = image.transform((width + 20, height + 10), Image.AFFINE, 
            (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)
    # 滤镜，边界加强
    image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image.save(SavePath)

if __name__ == '__main__':
    gene_code()
    