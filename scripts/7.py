
# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。


import os
import re



class Codestatistics:

    code_num = 0
    space_num = 0
    comment_num = 0
    Number_file=0
    py_namelist=[]
    py_list=[]

    def __init__(self, dirPath):
        self.dirPath = dirPath
        for i in os.listdir(dirPath):
            if os.path.splitext(i)[1] == '.py':  # 确保是.py
                self.py_namelist.append(i)

                with open(dirPath+'/'+i,  encoding='ISO-8859-15', mode='r+') as f:
                    data = f.read()
                    self.py_list.append(data)
        self.Number_file=len(self.py_list)

    def statistics():
        for i,data in enumerate(self.py_list):
            List_codeline = data.split("\n")
            for j in List_codeline:
                if "#" in j:




# print('the number of code is %d' % (num_code + num_empty + num_note))
# print('the number of empty is %d' % num_empty)
# print('the number of comment is %d' % num_note)





