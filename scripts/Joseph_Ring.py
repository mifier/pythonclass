# 约瑟夫环问题
# 按照如下规则去排除人：
#     所有人围成一圈
#     顺时针报数，每次报到q的人将被排除掉
#     被排除掉的人将从房间内被移走
#     然后从被kill掉的下一个人重新报数，继续报q，再清除，直到剩余一人


def Ring_outlist(inputlist, recount):
    outlist = []
    if type(inputlist).__name__ != 'list':
        raise ValueError("input must be a list!\n")
        
    index = 1
    while inputlist:
        data = inputlist.pop(0)
        if(index ==recount):
            outlist.append(data)
        else:
            inputlist.append(data)
        
        index += 1
        if(index == recount+1):
            index =1

    return outlist


def create_number_list(numbers):
    outlist = []
    for i in range(1,numbers+1):
        outlist.append(i)
    return outlist


if __name__ == "__main__":
    list = create_number_list(41)
    lifelist =Ring_outlist(list,3)
    print(lifelist)
    print('the last number: %d'%lifelist[-1])
