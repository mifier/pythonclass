
# �� 0005 �⣺ ����һ��Ŀ¼��װ�˺ܶ���Ƭ�������ǵĳߴ��ɶ������� iPhone5 �ֱ��ʵĴ�С

from PIL import Image
#PIL��Python Imaging Library ��ͼ��浵��������Ӧ�ó��������ѡ��������ʹ�øÿⴴ������ͼ�����ļ���ʽ֮�����ת������ӡͼ��ȡ�
import os.path
#os.path ģ����Ҫ���ڻ�ȡ�ļ������ԡ�


def Size(dirPath, size_x, size_y):
    #���庯��
    f_list = os.listdir(dirPath)
    # os.listdir() �������ڷ���ָ�����ļ��а�������ĸ˳����ļ����ļ��е����ֵ��б�
    for i in f_list:
        # �����б�
        if os.path.splitext(i)[1] == '.png' or os.path.splitext(i)[1] == '.jpg' or os.path.splitext(i)[1] == '.bmp' or os.path.splitext(i)[1] == '.jpeg' or os.path.splitext(i)[1] == '.gif' or os.path.splitext(i)[1] == '.psd' or os.path.splitext(i)[1] == '.tiff' or os.path.splitext(i)[1] == '.tga' or os.path.splitext(i)[1] == '.eps':
            #   os.path.splitext()�ָ�·��������·�������ļ���չ����Ԫ��
            img = Image.open(i)
            img.thumbnail((size_x, size_y))
            #  PILģ����Image��thumbnail()��������������������ͼ��������һ����Ԫ������Ϊ����ͼ�ĳߴ磬Ȼ��ʾ����С��ָ���ߴ硣
            img.save(i)
            print(i)


Size('D:\����\python\��Ŀ--1', 1136, 640)

