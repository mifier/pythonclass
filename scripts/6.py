#-*-coding:GBK -*-
#�� 0006 �⣺ ����һ��Ŀ¼��������һ���µ��ռǣ����� txt��Ϊ�˱���ִʵ����⣬�������ݶ���Ӣ�ģ���ͳ�Ƴ�����Ϊÿƪ�ռ�����Ҫ�Ĵʡ�


import os
import re


class Txts:
    txt_list=[]
    importantword_list=[]
    txt_namelist =[]
    def __init__(self, dirPath):
        self.dirPath = dirPath
        for i in os.listdir(dirPath):
            if os.path.splitext(i)[1] == '.txt':  # ȷ����txt
                self.txt_namelist.append(i)
                with open(dirPath+'/'+i,  encoding='ISO-8859-15', mode='r+') as f:
                    data = f.read()
                    self.txt_list.append(data)

    def find_importantword(self):
        for i,data in enumerate(self.txt_list):
            wordDict = dict()
            result = re.split('\W+', data)
            while result != []:
                word = result.pop()
                if len(word)<4: # С�ڳ���4�ĵ��ʲ�Ҫ
                    continue
                if word in wordDict:
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
                wordlist = sorted(wordDict.items(),key=lambda item: item[1], reverse=True) # ��word �������򣬴����ǰ

            print('file: %s->the most important word: \'%s\' ,the number is %d' %
                  (self.txt_namelist[i], wordlist[0][0], wordlist[0][1]))



if __name__ == '__main__':
    txts = Txts('./sources/txt')
    txts.find_importantword()


