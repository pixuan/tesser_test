# -*- coding: utf-8 -*-

import os
import subprocess


def image_to_string(img, out, cleanup=True, plus=''):
    # cleanup为True则识别完成后删除生成的文本文件
    # plus参数为给tesseract的附加高级参数
    cmd = 'tesseract ' + img + ' ' + out + ' -l chi_sim'
    subprocess.check_output(cmd, shell=True)  # 生成同名txt文件
    text = ''
    with open(out + '.txt', 'r') as f:
        text = f.read().strip()
    if cleanup:
        os.remove(out + '.txt')
    return text

image_to_string('/Users/pengzexin/Desktop/test.png', 'output')
