#!/usr/bin/env python3.4
# encoding: utf-8
"""
Created on 19-3-19
@title: '微信好友头像拼接'
@author: Xusl
"""
import itchat
import math
import PIL.Image as Image
import os

import logging.config

# from config import logger_path

# logging.config.fileConfig(logger_path)
# logger = logging.getLogger("root")


def photo_joint():
    # 微信登录
    func_name = u"好友头像拼接"
    # logger.info('start %s ' % func_name)
    itchat.auto_login(hotReload=True)
    itchat.dump_login_status()
    friends = itchat.get_friends(update=True)[0:]
    user = friends[0]["UserName"]

    #拼凑路径
    num = 0
    pwd_path = os.path.abspath(os.path.dirname(os.getcwd()))
    desc_photos = os.path.join(pwd_path, 'res/photos')
    desc_full = os.path.join(pwd_path, 'res')

    #保存微信头像（并不是使用urllib 进行图片下载）
    for i in friends:
        # UserName 微信系统内的用户编码标识
        img = itchat.get_head_img(userName=i["UserName"])
        file_image = open(desc_photos + "/" + str(num) + ".jpg", 'wb')
        file_image.write(img)
        file_image.close()
        num += 1

    ls = os.listdir(desc_photos)

    # 最后展示的头像都是正方形的，求出每个头像的长度
    each_size = int(math.sqrt(float(640 * 640) / len(ls)))  # 算出每张图片的大小多少合适
    lines = int(640 / each_size)
    image = Image.new('RGBA', (640, 640))   # 创建640*640px的大图
    x = 0
    y = 0

    for i in range(0, len(ls) + 1):
        try:
            img = Image.open(desc_photos + "/" + str(i) + ".jpg")
        except IOError:
            print("Error")
        else:
            # 单张图像变换大小
            img = img.resize((each_size, each_size), Image.ANTIALIAS)
            image.paste(img, (x * each_size, y * each_size))    # 粘贴位置
            x += 1
            if x == lines:  # 换行
                x = 0
                y += 1

    image.save(desc_full + u"/好友头像拼接图.png")
    itchat.send_image(desc_full + u"/好友头像拼接图.png", 'filehelper')     # 拼接完成发送给文件传输助手
    # logger.info('end %s ' % func_name)


def deal():
    """
    处理入口
    :return:
    """
    photo_joint()


if __name__ == '__main__':
    # deal()
    a = [2]
    b = []
    b.append(a)
    print b