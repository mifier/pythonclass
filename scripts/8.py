#-*-coding:GBK -*-
# �� 0008 �⣺ һ��HTML�ļ����ҳ���������ġ�
# https://www.cnblogs.com/hanmk/p/8724162.html

from bs4 import BeautifulSoup
with open("./sources/Yixiaohan_show-me-the-code_ Python.html", "r", encoding="utf-8") as f:
    html = f.read()
    # ʹ�� beautifulsoup �������ܣ�������ʹ��lxml
    soup = BeautifulSoup(html, "html.parser")
    
print(soup.title.string)  # ������⣬ǰ���Ǳ���������
print(soup.body)  # �������
print(soup.head)  # ���head������
print(soup.a)   # ��ȡhtml��a��ǩ����Ϣ(soup.aĬ�ϻ�ȡ��һ��a��ǩ�����ȡȫ������forѭ��ȥ����)
print(soup.a.string)   # ��ȡa��ǩ������
print(soup.prettify())     # ʹ��prettify()��ʽ����ʾ���

for u in soup.findAll('a'):  # ��ӡ����
    print(u['href'])

for j in soup.findAll('img'):  # ��ӡ����
    print(j['src'])

print('a��ǩ�����ǣ�', type(soup.a))   # �鿴a��ǩ������
print('��һ��a��ǩ�������ǣ�', soup.a.attrs)  # ��ȡa��ǩ����������(ע�⵽��ʽ���ֵ�)
print('a��ǩ���Ե������ǣ�', type(soup.a.attrs))  # �鿴a��ǩ���Ե�����
print('a��ǩ��class�����ǣ�', soup.a.attrs['class'])   # ��Ϊ���ֵ䣬ͨ���ֵ�ķ�ʽ��ȡa��ǩ��class����
print('a��ǩ��href�����ǣ�', soup.a.attrs['href'])   # ͬ����ͨ���ֵ�ķ�ʽ��ȡa��ǩ��href����
