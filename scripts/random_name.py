#-*-coding:GBK -*-
import random

peoplenumber=40


list_Xing = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王',
             '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '张', '李']
list_Ming = ['豫', '章', '故', '郡', '洪', '都', '新', '府', '星', '分', '翼', '轸', '地', '接', '衡', '庐', '襟', '三', '江', '', '而', '带', '五', '湖',
             '控', '蛮', '荆', '而', '引', '瓯', '越', '物', '华', '天', '宝', '龙', '光', '射', '牛', '斗', '之', '墟', '人', '杰', '地', '灵', '徐', '孺', '饯', '子']
list_studentname = []
for i in range(peoplenumber):
    name = random.choice(list_Xing)+random.choice(list_Ming) + \
        random.choice(list_Ming)
    list_studentname.append(name)
    #将随机生成的五个姓名生成一个列表list_student
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
#         list_gender.append('男')
#     else:
#         list_gender.append('女')
# for gender in list_gender:
#     print(gender)
#     pass
