
# �� 0011 �⣺ ���д��ı��ļ� filtered_words.txt�����������Ϊ�������ݣ����û��������д���ʱ�����ӡ�� Freedom�������ӡ�� Human Rights��



def load_txt(filename):
    with open(filename, encoding='utf-8', mode='r')as f:  # ���ļ�������f
        data = f.read()
    # split�ָ��ַ�����������ʽƥ��
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
