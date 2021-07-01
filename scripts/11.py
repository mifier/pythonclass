
# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。



def load_txt(filename):
    with open(filename, encoding='utf-8', mode='r')as f:  # 打开文件，记作f
        data = f.read()
    # split分割字符串，用正则公式匹配
    word_list = data.split('\n')
    return word_list


def judgment_Sensitivewords(Sensitivewords_list,input):
    for word in Sensitivewords_list:
        if word in input:
            print('Freedom')
            return
    print('Human Rights')




if __name__ == '__main__':
    Sensitivewords_list=load_txt('./sources/filtered_words.txt')
    judgment_Sensitivewords(Sensitivewords_list,input('input:\n'))
