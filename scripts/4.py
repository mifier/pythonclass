# �� 0004 �⣺ ��һ��Ӣ�ĵĴ��ı��ļ���ͳ�����еĵ��ʳ��ֵĸ�����


import re  #����


def get_word_num(TxtPath):
    with open(TxtPath, 'r')as f:  # ���ļ�������f
        data = f.read()
    result = re.split('\W+', data)  # split�ָ��ַ�����������ʽƥ��
    return len([x for x in result if x != ''])  # ���������������һ�Σ�ȥ�� ĩβ��


if __name__ == "__main__":
    word_num=get_word_num('./sources/english.txt')
    print(word_num)
    
