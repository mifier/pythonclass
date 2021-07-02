# 第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）
# 第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

import os
import json
import openpyxl
# from a12 import load_txt


def json_loadtxt(filename):
    with open(filename, encoding='gbk', mode='r')as f:
        text = f.read()
        text_json = json.loads(text)
    return text_json


def save_excel(content_dict,sheetname, excel_name):
    wb = openpyxl.Workbook()
   
    ws = wb.active  # 一般来说，表格大多数用到的是打开时显示的工作表，这时可以用active来获取当前工作表
    ws.title = sheetname

    for k, v in content_dict.items():
        #v.insert(0,k)
        if type(v) is not list:
            v=[v,]
        v[0:0]=k
        ws.append(v)
       

    wb.save(excel_name)


if __name__ == "__main__":
    content_dict = json_loadtxt("./sources/student.txt")
    save_excel(content_dict, 'student',"./sources/student.xlsx")
    content_dict = json_loadtxt("./sources/city.txt")
    save_excel(content_dict, 'city', "./sources/city.xlsx")
