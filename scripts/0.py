# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image, ImageDraw, ImageFont


def put_num_topright(picture, num):
    img = Image.open(picture)  
    draw = ImageDraw.Draw(img)
    x,_ = img.size  # 获得尺寸
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 200)  # 字体设置,第二个为字体大小
    fillcolor = "#ff0000"  # 颜色设置,  红色
    draw.text((x - 200, 100), str(num), font=font, fill=fillcolor)  # 添加文字
    img.save('./soures/QQ_Modify.jpg', 'jpeg')  # 保存修改后图片


if __name__ == '__main__':
    picture = './soures/QQ.jpg'
    num = 6
    put_num_topright(picture, num)
