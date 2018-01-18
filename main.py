# -*- coding: utf-8 -*-
from aitext import Ai
from image_processer import ImageProcesser


def main():
    img_pro = ImageProcesser()
    titles = img_pro.get_img_content()
    issue = ''   # 问题
    answer = ['', '', '', '', '', ''] # 答案
    countone = 0
    answercount = 0
    for title in titles:
        countone += 1
        if countone >= len(titles) - 2:
            answer[answercount] = title['words']
            answercount += 1
        else:
            issue = issue + title['words']

    print(issue)  # 打印问题
    print('  A:' + answer[0] + ' B:' + answer[1] + ' C:' + answer[2])  # 打印问题
    ai = Ai(issue, answer)
    ai.search()


if __name__ == '__main__':
    main()
