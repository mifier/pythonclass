#-*-coding:GBK -*-
#第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。


import os
import re


class Txts:
    txt_list=[]
    importantword_list=[]
    txt_namelist =[]
    def __init__(self, dirPath):
        self.dirPath = dirPath
        for i in os.listdir(dirPath):
            if os.path.splitext(i)[1] == '.txt':  # 确保是txt
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
                if len(word)<4: # 小于长度4的单词不要
                    continue
                if word in wordDict:
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
                wordlist = sorted(wordDict.items(),key=lambda item: item[1], reverse=True) # 以word 计数排序，大的在前

            print('file: %s->the most important word: \'%s\' ,the number is %d' %
                  (self.txt_namelist[i], wordlist[0][0], wordlist[0][1]))



if __name__ == '__main__':
    txts = Txts('./sources/txt')
    txts.find_importantword()


