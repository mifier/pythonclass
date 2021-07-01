# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。


def load_txt(filename):
    with open(filename, encoding='utf-8', mode='r')as f:  # 打开文件，记作f
        data = f.read()
    # split分割字符串，用正则公式匹配
    word_list = data.split('\n')
    return word_list


def shield_Sensitivewords(Sensitivewords_list, input):
    for word in Sensitivewords_list:
        if word in input:
            input = input.replace(word, "**")
            
    print('output:\n'+input)


if __name__ == '__main__':
    Sensitivewords_list = load_txt('./sources/filtered_words.txt')
    shield_Sensitivewords(Sensitivewords_list, input('input:\n'))



