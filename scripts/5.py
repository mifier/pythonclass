#-*-coding:GBK -*-
# �� 0005 �⣺ ����һ��Ŀ¼��װ�˺ܶ���Ƭ�������ǵĳߴ��ɶ������� iPhone5 �ֱ��ʵĴ�С

from PIL import Image
import os.path
#os.path ģ����Ҫ���ڻ�ȡ�ļ������ԡ�


class Pictures:
    picture_extension=['.png','.jpg','.bmp','.jpeg','.gif']
    picture_list=[]
    picture_namelist=[]
    def __init__(self, dirPath):
        self.dirPath = dirPath
        for i in os.listdir(dirPath):
            if os.path.splitext(i)[1] in self.picture_extension :# ȷ����ͼƬ
                self.picture_namelist.append(i)
                img = Image.open(dirPath+'/'+i)
                self.picture_list.append(img)


    def Set_allpicturesize(self, size_x, size_y):
        for i,picture in enumerate(self.picture_list):
            picture.thumbnail((size_x, size_y)) #  PILģ����Image��thumbnail()��������������������ͼ��������һ����Ԫ������Ϊ����ͼ�ĳߴ磬Ȼ��ʾ����С��ָ���ߴ硣   
            picture.save(self.dirPath+'/resize(%d, %d)_' %(size_x, size_y)+self.picture_namelist[i]) # ������


if __name__ == '__main__':
    pictures=Pictures('./sources/photo')
    pictures.Set_allpicturesize(1136, 640)

