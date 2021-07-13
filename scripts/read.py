# -*-coding:GBK -*-

import csv
import openpyxl
from collections import deque

# ��csv�ļ���д������
# with open("./sources/people.csv", 'a') as f:
#     row = ['��Խ��', '100006', '21', '��', '186']
#     write = csv.writer(f)
#     write.writerow(row)



class Reader(object):
    reader_list = []

    def __getitem__(self, index):
        return self.reader_list[index]

    def Joseph_ring(self, recount, startpoint=1):
      inputlist = deque(self.reader_list)
      len_inputlist = len(inputlist)
      outlist = []
       # ��ʼ�����
      if startpoint > 0:
          
        inputlist.rotate(-startpoint+1)
      elif startpoint < 0:
            inputlist.rotate(-startpoint)
        # ����������
      for i in range(len_inputlist):
            if recount > 0:
                inputlist.rotate(-recount+1)
            elif recount < 0:
                inputlist.rotate(-recount)
            outlist.append(inputlist.popleft())

        # outlist.reverse()   # ��ת���� δʹ��
      self.outlist = outlist



class CSV_reader(Reader):
    def __init__(self,filename):
        with open(filename) as f:
            reader = csv.reader(f)
            self.reader_list = [row for row in reader]
            
class Excel_reader(Reader):
    def __init__(self,filename):
        wb=openpyxl.load_workbook(filename)
        sheet = wb.active
        sheet_list = list(sheet.rows)
        for row in sheet_list:
            cow_list=[]
            for cell in row:
                cow_list.append(cell.value)
            self.reader_list.append(cow_list)

class Zip_reader(Reader):
    def __init__(self,filename):
        a=0


if __name__ == "__main__":
    data=CSV_reader("./sources/people.csv")
    
    for i in data:
        print (i)

    data1=Excel_reader("./sources/people.xlsx")
    

