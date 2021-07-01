# 第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。


import re  #正则


def get_word_num(TxtPath):
    with open(TxtPath, 'r')as f:  # 打开文件，记作f
        data = f.read()
    result = re.split('\W+', data)  # split分割字符串，用正则公式匹配
    return len([x for x in result if x != ''])  # 输出单词数，历遍一次，去除 末尾空


if __name__ == "__main__":
    word_num=get_word_num('./sources/english.txt')
    print(word_num)
    
