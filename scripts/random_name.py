#-*-coding:GBK -*-
import random

peoplenumber=40


list_Xing = ['��', 'Ǯ', '��', '��', '��', '��', '֣', '��',
             '��', '��', '��', '��', '��', '��', '��', '��', '��', '��']
list_Ming = ['ԥ', '��', '��', '��', '��', '��', '��', '��', '��', '��', '��', '��', '��', '��', '��', '®', '��', '��', '��', '', '��', '��', '��', '��',
             '��', '��', '��', '��', '��', '�', 'Խ', '��', '��', '��', '��', '��', '��', '��', 'ţ', '��', '֮', '��', '��', '��', '��', '��', '��', '��', '��', '��']
list_studentname = []
for i in range(peoplenumber):
    name = random.choice(list_Xing)+random.choice(list_Ming) + \
        random.choice(list_Ming)
    list_studentname.append(name)
    #��������ɵ������������һ���б�list_student
for studentname in list_studentname:
    print (studentname)
    pass

list_age=[]
for i in range(peoplenumber):
    age = random.randint(165,195)
    list_age.append(age)
for age in list_age:
    print(age)
    pass

# list_gender=[]
# for i in range(peoplenumber):
#     gender = random.randint(0, 1)
#     if gender==0:
#         list_gender.append('��')
#     else:
#         list_gender.append('Ů')
# for gender in list_gender:
#     print(gender)
#     pass
