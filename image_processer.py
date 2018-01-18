# -*- coding: utf-8 -*-
import os
from PIL import Image
from cmd_tesser import CmdTesser


class ImageProcesser(object):

    def get_screenshot(self):
        os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
        os.system("adb pull /sdcard/screenshot.png ./screenshot.png")
        im = Image.open(r"./screenshot.png")
        img_size = im.size
        w = im.size[0]
        h = im.size[1]
        print("xx:{}".format(img_size))
        region = im.crop((70, 200, w - 70, 700))  # 裁剪的区域
        region.save(r"./crop_test1.png")

    def get_img_content(self):
        self.get_screenshot()
        cmd_tesser = CmdTesser()
        text = cmd_tesser.image_to_string(r"./screenshot.png", 'output')
        return text
