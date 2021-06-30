
# 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小

from PIL import Image
#PIL是Python Imaging Library 是图像存档和批处理应用程序的理想选择。您可以使用该库创建缩略图，在文件格式之间进行转换，打印图像等。
import os.path
#os.path 模块主要用于获取文件的属性。


def Size(dirPath, size_x, size_y):
    #定义函数
    f_list = os.listdir(dirPath)
    # os.listdir() 方法用于返回指定的文件夹包含以字母顺序的文件或文件夹的名字的列表。
    for i in f_list:
        # 遍历列表
        if os.path.splitext(i)[1] == '.png' or os.path.splitext(i)[1] == '.jpg' or os.path.splitext(i)[1] == '.bmp' or os.path.splitext(i)[1] == '.jpeg' or os.path.splitext(i)[1] == '.gif' or os.path.splitext(i)[1] == '.psd' or os.path.splitext(i)[1] == '.tiff' or os.path.splitext(i)[1] == '.tga' or os.path.splitext(i)[1] == '.eps':
            #   os.path.splitext()分割路径，返回路径名和文件扩展名的元组
            img = Image.open(i)
            img.thumbnail((size_x, size_y))
            #  PIL模块中Image类thumbnail()方法可以用来制作缩略图，它接受一个二元数组作为缩略图的尺寸，然后将示例缩小到指定尺寸。
            img.save(i)
            print(i)


Size('D:\工作\python\项目--1', 1136, 640)

