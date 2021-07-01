#-*-coding:GBK -*-
# 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小

from PIL import Image
import os.path
#os.path 模块主要用于获取文件的属性。


class Pictures:
    picture_extension=['.png','.jpg','.bmp','.jpeg','.gif']
    picture_list=[]
    picture_namelist=[]
    def __init__(self, dirPath):
        self.dirPath = dirPath
        for i in os.listdir(dirPath):
            if os.path.splitext(i)[1] in self.picture_extension :# 确保是图片
                self.picture_namelist.append(i)
                img = Image.open(dirPath+'/'+i)
                self.picture_list.append(img)


    def Set_allpicturesize(self, size_x, size_y):
        for i,picture in enumerate(self.picture_list):
            picture.thumbnail((size_x, size_y)) #  PIL模块中Image类thumbnail()方法可以用来制作缩略图，它接受一个二元数组作为缩略图的尺寸，然后将示例缩小到指定尺寸。   
            picture.save(self.dirPath+'/resize(%d, %d)_' %(size_x, size_y)+self.picture_namelist[i]) # 重命名


if __name__ == '__main__':
    pictures=Pictures('./sources/photo')
    pictures.Set_allpicturesize(1136, 640)

