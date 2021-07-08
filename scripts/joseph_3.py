# -*-coding:GBK -*-
# 学有余力的同学，将约瑟夫环作为容器，用for遍历。

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


class Joseph_Ring(deque):
    def __init__(self, input_list, recount, startpoint=1):
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
            
        # outlist.reverse()   # 反转队列 未使用
        super().extend(outlist)


if __name__ == "__main__":
    numbers = 34
    recount = 4
    people_list = load_excellist('./sources/people.xlsx')
    people_list = people_list[0:numbers]

    people_objectlist = [People(i) for i in people_list]

    ring = Joseph_Ring(people_objectlist, recount)

    for i in ring:
        i.printself()
    
    a=ring.pop()
    print('活到最后的人是：',end='')
    a.printself()

    pass
