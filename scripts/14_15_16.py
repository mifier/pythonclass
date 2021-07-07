# �� 0014 �⣺ ���ı��ļ� student.txtΪѧ����Ϣ, ��������ݣ����������ţ�
# �� 0015 �⣺ ���ı��ļ� city.txtΪ������Ϣ, ��������ݣ����������ţ�������ʾ��
# �� 0016 �⣺ ���ı��ļ� numbers.txt, ��������ݣ����������ţ�������ʾ��

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
   
    ws = wb.active  # һ����˵����������õ����Ǵ�ʱ��ʾ�Ĺ�������ʱ������active����ȡ��ǰ������
    ws.title = sheetname


    if type(content_dict).__name__ == 'dict':
        for k, v in content_dict.items():
            #v.insert(0,k)
            if type(v).__name__ != 'list':
                v = [v, ]
            v[0:0]=k
            ws.append(v)

    if type(content_dict).__name__ == 'list':
        for  v in content_dict:
            #v.insert(0,k)
            if type(v).__name__ != 'list':
                v = [v, ]
            
            ws.append(v)



        wb.save(excel_name)


if __name__ == "__main__":
    content_dict = json_loadtxt("./sources/student.txt")
    save_excel(content_dict, 'student',"./sources/student.xlsx")
    content_dict = json_loadtxt("./sources/city.txt")
    save_excel(content_dict, 'city', "./sources/city.xlsx")
    content_dict = json_loadtxt("./sources/numbers.txt")
    save_excel(content_dict, 'numbers', "./sources/numbers.xlsx")
