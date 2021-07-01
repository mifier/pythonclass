
# 第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random
import string


# 随机生成大小写字母
def random_letter():
    return(random.choice(string.ascii_letters))

# 随机生成背景色对应的RGB值
def random_BlackgroundColor():
    return(random.randint(30, 255), random.randint(30, 255), random.randint(30, 255))   #[] 区间越接近0越暗，越接近255越亮


# 随机生成字体颜色
def random_WordColor():
    return(random.randint(30, 127), random.randint(30, 127), random.randint(30, 127))  #字体浅色



def create_Image(size_x, size_y,num_letters):
    font_size=int(size_y*0.75)

    if size_x < num_letters*font_size+50 or size_y < 60:
        print("The size entered is too small!")
        return

    img = Image.new("RGB", (size_x, size_y), (255, 255, 255))
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', font_size)
    draw = ImageDraw.Draw(img)
    for x in range(size_x):
        for y in range(size_y):
            draw.point((x, y), random_BlackgroundColor())

    words = ""
    spacing = size_x//(num_letters+1)
    for i in range(num_letters):
        word = random_letter()
        draw.text((10+spacing * i + random.randint(0, spacing),
                     random.randint(0, int(size_y*0.25))),word, font=font, fill=random_WordColor())
        words += word

    img = img.filter(ImageFilter. GaussianBlur(radius=2))  # 高斯模糊 radius指定平滑半径
    img.save("./sources/VerificationCode_%s.png" % words)
    print(words)


if __name__ == "__main__":
    create_Image(300, 80, num_letters=4)
