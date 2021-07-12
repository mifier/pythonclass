# -*-coding:GBK -*-
# ѧ��������ͬѧ����Լɪ����Ϊ��������for������

import openpyxl
from collections import deque

# ��excel���У�ȡ�����ƣ�Ԫ��


def load_excellist(filename):

    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    # ȡ��һ��
    sheet_list = list(sheet.rows)
    sheet_key = [i.value for i in sheet_list[0]]
    len_key = len(sheet_key)

    # ȡvalue �����ֵ�
    len_people = len(sheet_list)-1
    if(len_people == 0):
        raise "excel��û������\n"

    sheet_list = []
    for row in sheet_list[1:]:
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

    def printself(self):   # ��ӡ���������
        name_list = [e for e in self.__dict__ if not e.startswith('_')]
        print(['%s:' % i + str(eval('self.%s' %
                                    i, {'self': self})) for i in name_list])


class Joseph_Ring(deque):
    def __init__(self, input_list, recount, startpoint=1):
        inputlist = deque()
        inputlist.extend(input_list)
        len_inputlist = len(inputlist)
        outlist = []
        # ��ʼ�����
        if startpoint > 0:
            inputlist.rotate(startpoint-1)
        elif startpoint < 0:
            inputlist.rotate(startpoint)
        # ����������
        for i in range(len_inputlist):
            if recount > 0:
                inputlist.rotate(-recount+1)
            elif recount < 0:
                inputlist.rotate(-recount)
            outlist.append(inputlist.popleft())
            
        # outlist.reverse()   # ��ת���� δʹ��
        self.extend(outlist)


if __name__ == "__main__":
    numbers = 34
    recount = 4
    people_list = load_excellist('./sources/people.xlsx')
    people_list = people_list[0:numbers]

    people_objectlist = [People(i) for i in people_list]

    Joseph_ring = Joseph_Ring(people_objectlist, recount)

    for i in Joseph_ring:
        i.printself()
    
    a = Joseph_ring.pop()
    print('��������ǣ�',end='')
    a.printself()

    pass
