
# �� 0010 �⣺ ʹ�� Python ������������ͼ�е���ĸ��֤��ͼƬ

from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random
import string


# ������ɴ�Сд��ĸ
def random_letter():
    return(random.choice(string.ascii_letters))

# ������ɱ���ɫ��Ӧ��RGBֵ
def random_BlackgroundColor():
    return(random.randint(30, 255), random.randint(30, 255), random.randint(30, 255))   #[] ����Խ�ӽ�0Խ����Խ�ӽ�255Խ��


# �������������ɫ
def random_WordColor():
    return(random.randint(30, 127), random.randint(30, 127), random.randint(30, 127))  #����ǳɫ



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

    img = img.filter(ImageFilter. GaussianBlur(radius=2))  # ��˹ģ�� radiusָ��ƽ���뾶
    img.save("./sources/VerificationCode_%s.png" % words)
    print(words)


if __name__ == "__main__":
    create_Image(300, 80, num_letters=4)
