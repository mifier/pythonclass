#-*-coding:GBK -*-
# 第 0008 题： 一个HTML文件，找出里面的正文。
# https://www.cnblogs.com/hanmk/p/8724162.html

from bs4 import BeautifulSoup
with open("./sources/Yixiaohan_show-me-the-code_ Python.html", "r", encoding="utf-8") as f:
    html = f.read()
    # 使用 beautifulsoup 解析功能，解析器使用lxml
    soup = BeautifulSoup(html, "html.parser")
    
print(soup.title.string)  # 输出标题，前提是标题必须存在
print(soup.body)  # 输出正文
print(soup.head)  # 输出head的内容
print(soup.a)   # 获取html的a标签的信息(soup.a默认获取第一个a标签，想获取全部就用for循环去遍历)
print(soup.a.string)   # 获取a标签的名字
print(soup.prettify())     # 使用prettify()格式化显示输出

for u in soup.findAll('a'):  # 打印链接
    print(u['href'])

for j in soup.findAll('img'):  # 打印链接
    print(j['src'])

print('a标签类型是：', type(soup.a))   # 查看a标签的类型
print('第一个a标签的属性是：', soup.a.attrs)  # 获取a标签的所有属性(注意到格式是字典)
print('a标签属性的类型是：', type(soup.a.attrs))  # 查看a标签属性的类型
print('a标签的class属性是：', soup.a.attrs['class'])   # 因为是字典，通过字典的方式获取a标签的class属性
print('a标签的href属性是：', soup.a.attrs['href'])   # 同样，通过字典的方式获取a标签的href属性
