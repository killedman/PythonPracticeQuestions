#! /usr/bin/env python
# -*- coding: utf8 -*-

# author: dreampython
# date: 2018-10-22
# 第 0005 题： 你有一个目录，装了很多照片，
# 把它们的尺寸变成都不大于 iPhone5 分辨率的大小
# iphone5的分辨率大小： 320*568

from PIL import Image
import os
import imghdr

# iphone5分辨率大小
iphone_size = (320, 568)

# 获取目录中所有的图片文件
def get_image_file(image_path):
    image_files = []
    image_type_tuple = ('jpeg', 'png', 'gif', 'bmp')
    if os.path.exists(image_path):
        for root,dirs,files in os.walk(image_path):
            for file in files:
                filepath = os.path.join(root, file)
                imgType = imghdr.what(filepath)
                if imgType in image_type_tuple:
                    image_files.append(filepath)
    else:
        print('please check ' + image_path + ' if exist')
    return image_files

# 获取imagefile的size
def get_imagefile_size(imagefile):
    img = Image.open(imagefile)
    return  img.size

# 获取大于iphone5分辨率的图片
def get_bigger_image_file(iphone_size,image_files):
    bigger_image_files = []
    for imagefile in image_files:
        img_size = get_imagefile_size(imagefile)
        if img_size[0] > iphone_size[0] or img_size[1] > iphone_size[1]:
            bigger_image_files.append(imagefile)
    return bigger_image_files

# 重新生成图片
def gen_image_again(target_files, iphone_size, target_dir):
    print('begin save new image...')
    for target_file in target_files:
        image = Image.open(target_file)
        # 获取缩放率
        radio = min(iphone_size[0]/image.size[0],iphone_size[1]/image.size[1])
        # ANTIALIAS 抗锯齿模式
        image = image.resize((int(image.size[0] * radio),\
            int(image.size[1] * radio)),Image.ANTIALIAS)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        outfile = os.path.join(target_dir, os.path.basename(target_file))
        image.save(outfile,imghdr.what(target_file))
    print('all new image alread saved.')

if __name__ == "__main__":
    image_path = input('please input store image \'s dir path: ')
    target_dir = input('please input new image save dir: ')
    image_files = get_image_file(image_path)
    target_files = get_bigger_image_file(iphone_size,image_files)
    gen_image_again(target_files,iphone_size,target_dir)