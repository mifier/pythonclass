# -*-coding:GBK -*-

# n=1 开始
# def josephus(n, q): return 1 if n == 1 else (josephus(n-1, q) + q-1) % n +1

# print(josephus(46, 4))

# 约瑟夫环第二次作业要求：
# 1、使用容器作为输入，容器中每个元素都是个对象，对象的属性和方法自定义，基础属性包括姓名、学号。输入要包括间隔、起始位置。


import openpyxl
from collections import deque

# 将excel的列，取出名称，元素


def load_excellist(filename):

    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    # 取第一行
    sheet_key = [i.value for i in list(sheet.rows)[0]]
    len_key = len(sheet_key)

    # 取value 生成字典
    len_people = len(list(sheet.rows))-1
    if(len_people == 0):
        raise "excel中没有数据\n"

    sheet_list = []
    for row in list(sheet.rows)[1:]:
        dic = {}
        assert len(row) == len_key
        for i, cell in enumerate(row):
            dic[sheet_key[i]] = cell.value
        sheet_list.append(dic)

    return sheet_list


class People:
    def __init__(self, people_dic):
        for key, value in people_dic.items():
            exec('self.%s = value' % (key), {'self': self, 'value': value})

    def printself(self):   # 打印自身的属性
        name_list = [e for e in self.__dict__ if not e.startswith('_')]
        print(['%s:' % i + str(eval('self.%s' %
              i, {'self': self})) for i in name_list])

# 可以双向取值，起点等效队列，可用负数
def Ring_outlist(input_list, recount, startpoint=1):

    inputlist = deque()
    inputlist.extend(input_list)
    len_inputlist = len(inputlist)
    outlist = []

    # 初始化起点
    if startpoint > 0:
        inputlist.rotate(startpoint-1)
    elif startpoint < 0:
        inputlist.rotate(startpoint)
    # 获得输出队列
    for i in range(len_inputlist):
        if recount > 0:
          inputlist.rotate(-recount+1)
        elif recount < 0:
          inputlist.rotate(-recount)
        outlist.append(inputlist.popleft())

    return outlist



if __name__ == "__main__":
    numbers = 34
    recount = 4

    people_list = load_excellist('./sources/people.xlsx')
    people_list = people_list[0:numbers]
    people_objectlist=[People(i) for i in people_list]
    life_list = Ring_outlist(people_objectlist, recount)

    a = life_list.pop()
    a.printself()
    pass
