#-*-coding:GBK -*-
#�� 0001 �⣺ ��Ϊ Apple Store App ���������ߣ���Ҫ����ʱ������Ϊ���Ӧ�����ɼ����루�����Ż�ȯ����ʹ�� Python ������� 200 �������루�����Ż�ȯ����


import random
import hashlib  # ʹ��MD5���ɼ�����


def get_Activationcode(Activationcode_num):
    list_activation = []
    for i in range(Activationcode_num):
        string_activation=str(random.randint(10000,99999))  #����һ��5λ�����
        string_activation += "������"+"0000"+str(i*1000)    #����i ȷ�����ظ�
        activation_code = hashlib.md5(string_activation.encode(encoding='UTF-8')).hexdigest()
        list_activation.append(activation_code)

    return list_activation


if __name__ == '__main__':
    List_Activationcode = get_Activationcode(Activationcode_num=200)
    for code in List_Activationcode:
        print(code)
    output = open('./sources/List_Activationcode.txt', 'w+') # ������txt
    for i in range(len(List_Activationcode)):    
        output.write(str(List_Activationcode[i]))
        output.write('\n')
    output.close()












