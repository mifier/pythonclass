#-*-coding:GBK -*-
#第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？


import random
import hashlib  # 使用MD5生成激活码


def get_Activationcode(Activationcode_num):
    list_activation = []
    for i in range(Activationcode_num):
        string_activation=str(random.randint(10000,99999))  #加入一个5位随机数
        string_activation += "激活码"+"0000"+str(i*1000)    #加入i 确保不重复
        activation_code = hashlib.md5(string_activation.encode(encoding='UTF-8')).hexdigest()
        list_activation.append(activation_code)

    return list_activation


if __name__ == '__main__':
    List_Activationcode = get_Activationcode(Activationcode_num=200)
    for code in List_Activationcode:
        print(code)
    output = open('./sources/List_Activationcode.txt', 'w+') # 导出到txt
    for i in range(len(List_Activationcode)):    
        output.write(str(List_Activationcode[i]))
        output.write('\n')
    output.close()












