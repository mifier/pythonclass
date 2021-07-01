# �� 0012 �⣺ ���д��ı��ļ� filtered_words.txt����������� �� 0011��һ�������û��������д������ �Ǻ� * �滻�����統�û����롸�����Ǹ��ó��С������ɡ�**�Ǹ��ó��С���


def load_txt(filename):
    with open(filename, encoding='utf-8', mode='r')as f:  # ���ļ�������f
        data = f.read()
    # split�ָ��ַ�����������ʽƥ��
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



