# -*-coding:GBK -*-

import csv
import openpyxl


# 向csv文件中写入数据
# with open("./sources/people.csv", 'a') as f:
#     row = ['李越宝', '100006', '21', '男', '186']
#     write = csv.writer(f)
#     write.writerow(row)



class Reader(object):
    reader_list = []

    def __getitem__(self, index):
        return self.reader_list[index]

    def item2dict(self):
      print(self.reader_list[0])

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
    data.list2dict()
    for i in data:
        print (i)

    data1=Excel_reader("./sources/people.xlsx")
    data1.list2dict()

