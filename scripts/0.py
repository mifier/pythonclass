# �� 0000 �⣺ ����� QQ ͷ�񣨻���΢��ͷ�����ϽǼ��Ϻ�ɫ�����֣�������΢��δ����Ϣ����������ʾЧ���� ������ͼ��Ч��

from PIL import Image, ImageDraw, ImageFont


def put_num_topright(picture, num):
    img = Image.open(picture)  
    draw = ImageDraw.Draw(img)
    x,_ = img.size  # ��óߴ�
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 200)  # ��������,�ڶ���Ϊ�����С
    fillcolor = "#ff0000"  # ��ɫ����,  ��ɫ
    draw.text((x - 200, 100), str(num), font=font, fill=fillcolor)  # �������
    img.save('./soures/QQ_Modify.jpg', 'jpeg')  # �����޸ĺ�ͼƬ


if __name__ == '__main__':
    picture = './soures/QQ.jpg'
    num = 6
    put_num_topright(picture, num)
