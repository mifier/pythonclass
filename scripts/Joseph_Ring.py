# -*-coding:GBK -*-
# Լɪ������
# �������¹���ȥ�ų��ˣ�
#     ������Χ��һȦ
#     ˳ʱ�뱨����ÿ�α���q���˽����ų���
#     ���ų������˽��ӷ����ڱ�����
#     Ȼ��ӱ�kill������һ�������±�����������q���������ֱ��ʣ��һ��

'''
ÿ��ѭ��һ����ʱ�临�Ӷ�O��nq��
�����٣�����ʱ���
'''


def Ring_outlist1(input_list, recount):
    inputlist = input_list.copy()
    outlist = []

    if type(inputlist).__name__ != 'list':
        raise ValueError("input must be a list!\n")

    index = 1
    while inputlist:
        data = inputlist.pop(0)
        if(index == recount):
            outlist.append(data)
        else:
            inputlist.append(data)

        index += 1
        if(index == recount+1):
            index = 1

    return outlist


'''
ÿ��ѭ��q����ʱ�临�Ӷ�O��n��
����࣬����ʱ���
'''


def Ring_outlist2(input_list, recount):
    inputlist = input_list.copy()
    outlist = []
    if type(inputlist).__name__ != 'list':
        raise ValueError("input must be a list!\n")

    while len(inputlist) >= recount:
        data_list = inputlist[0:recount]
        del inputlist[0:recount]
        data = data_list.pop()
        inputlist.extend(data_list)
        outlist.append(data)

    while inputlist:
        index = recount % len(inputlist)
        if index == 0:
            outlist.append(inputlist.pop())
        else:
            data_list = inputlist[0:index]
            del inputlist[0:index]
            data = data_list.pop()
            inputlist.extend(data_list)
            outlist.append(data)

    return outlist


def create_number_list(numbers):
    outlist = []
    for i in range(1, numbers+1):
        outlist.append(i)
    return outlist


if __name__ == "__main__":
    numbers = 46
    recount = 4

    list = create_number_list(numbers)
    lifelist1 = Ring_outlist1(list, recount)
    print(lifelist1)
    print('the last number: %d \n' % lifelist1[-1])

    lifelist2 = Ring_outlist2(list, recount)
    print(lifelist2)
    print('the last number: %d \n' % lifelist2[-1])
