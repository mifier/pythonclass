
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

                with open(dirPath+'/'+i,  encoding='gbk', mode='r+') as f:  # 中文不乱码
                    data = f.read()
                    self.py_list.append(data)
        self.Number_file=len(self.py_list)

    def statistics(self):
        for i,data in enumerate(self.py_list):
            List_codeline = data.split("\n")
            for j in List_codeline:
                if j.isspace() or j=='':
                    self.space_num+=1
                elif '#' in j:
                    self.comment_num+=1
                    search1 = re.search('(\w+)', j).span()
                    search2 = re.search(r'(#)', j).span()
                    if search1[0]<search2[0]:
                        self.code_num += 1                  
                else :
                    self.code_num+=1

    def print(self):
        print('the number of code is %d' %
              (self.code_num + self.space_num + self.comment_num))
        print('the number of empty is %d' % self.space_num)
        print('the number of comment is %d' % self.comment_num)


if __name__ == '__main__':
    codestatistics = Codestatistics('./scripts')
    codestatistics.statistics()
    codestatistics.print()








