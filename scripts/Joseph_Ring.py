# -*-coding:GBK -*-
# 约瑟夫环问题
# 按照如下规则去排除人：
#     所有人围成一圈
#     顺时针报数，每次报到q的人将被排除掉
#     被排除掉的人将从房间内被移走
#     然后从被kill掉的下一个人重新报数，继续报q，再清除，直到剩余一人

'''
每次循环一个，时间复杂度O（nq）
代码少，花的时间多
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
每次循环q个，时间复杂度O（n）
代码多，花的时间短
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
    numbers = 34
    recount = 4

    list = create_number_list(numbers)
    # list.append('sjd')
    life_list1 = Ring_outlist1(list, recount)
    print(life_list1)
    print('the last number: %d \n' % life_list1[-1])

    life_list2 = Ring_outlist2(list, recount)
    print(life_list2)
    print('the last number: %d \n' % life_list2[-1])
