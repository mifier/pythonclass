# Լɪ������
# �������¹���ȥ�ų��ˣ�
#     ������Χ��һȦ
#     ˳ʱ�뱨����ÿ�α���q���˽����ų���
#     ���ų������˽��ӷ����ڱ�����
#     Ȼ��ӱ�kill������һ�������±�����������q���������ֱ��ʣ��һ��


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
