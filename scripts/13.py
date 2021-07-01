#-*-coding:GBK -*-
# 第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)

import requests
import re
from bs4 import BeautifulSoup


# 获得所有的img对象
def get_img_list(webUrl):
    res = requests.get(webUrl)
    res.encoding = 'gbk'   # 解决中文乱码
    # 解析网页
    soup = BeautifulSoup(res.text, 'html.parser')
    list= soup.select('img')
    
    img_List=[]
    for item in list:
        img_List.append(item.attrs['src'])
    return img_List

# 保存网址对应的图片到指定目录
def listSave(picList, download_dir):
    i = 1
    for img in picList:
        extend = re.search('([.][jgbp][a-zA-Z]+)', img).group(0)  # 获得扩展名
        try:
            pic = requests.get(img, timeout=5)
            if pic.status_code == 200:
                fp = open(download_dir + str(i)+extend, 'wb')
                fp.write(pic.content)  # 写入图片
                fp.close()
                i += 1
        except requests.exceptions.ConnectionError:
            print("图片无法下载")
            continue
        except requests.exceptions.MissingSchema:
            print("地址无法访问")
            continue


if __name__ == '__main__':
    img_List = get_img_list('http://www.netbian.com/weimei/')
    download_dir = './sources/CrawlingPictures/'
    listSave(img_List, download_dir)
