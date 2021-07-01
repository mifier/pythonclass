#-*-coding:GBK -*-
# �� 0013 �⣺ �� Python дһ����ͼƬ�ĳ����� �����������ձ�����ͼƬ :-)

import requests
import re
from bs4 import BeautifulSoup


# ������е�img����
def get_img_list(webUrl):
    res = requests.get(webUrl)
    res.encoding = 'gbk'   # �����������
    # ������ҳ
    soup = BeautifulSoup(res.text, 'html.parser')
    list= soup.select('img')
    
    img_List=[]
    for item in list:
        img_List.append(item.attrs['src'])
    return img_List

# ������ַ��Ӧ��ͼƬ��ָ��Ŀ¼
def listSave(picList, download_dir):
    i = 1
    for img in picList:
        extend = re.search('([.][jgbp][a-zA-Z]+)', img).group(0)  # �����չ��
        try:
            pic = requests.get(img, timeout=5)
            if pic.status_code == 200:
                fp = open(download_dir + str(i)+extend, 'wb')
                fp.write(pic.content)  # д��ͼƬ
                fp.close()
                i += 1
        except requests.exceptions.ConnectionError:
            print("ͼƬ�޷�����")
            continue
        except requests.exceptions.MissingSchema:
            print("��ַ�޷�����")
            continue


if __name__ == '__main__':
    img_List = get_img_list('http://www.netbian.com/weimei/')
    download_dir = './sources/CrawlingPictures/'
    listSave(img_List, download_dir)
