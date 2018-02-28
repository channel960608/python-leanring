#验证码生成
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

#随机字母
def rndChar():
    return chr(random.randint(65, 90))

#随机颜色32
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#随机颜色64
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
#创建font对象
font = ImageFont.truetype('Arial.ttf', 36)
#创建Draw对象
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=(rndColor()))
#输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
#模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
