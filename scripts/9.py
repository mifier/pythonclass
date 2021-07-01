# �� 0009 �⣺ һ��HTML�ļ����ҳ���������ӡ�

import re
import os


def find_handle(htmlpath):
    with open(htmlpath, "r", encoding="utf-8") as f:
        html = f.read()
    pattern = (r'([hftps]+://\S*)"')
    for i in (re.findall(pattern, html)):
        print(i)


if __name__ == "__main__":
    htmlpath = "./sources/Yixiaohan_show-me-the-code_ Python.html"
    find_handle(htmlpath)
