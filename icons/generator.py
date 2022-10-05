from random import random
from PIL import Image, ImageDraw
from datetime import datetime


def generate_icon():
    image = Image.new('RGB', (256, 256), '#101010')
    draw = ImageDraw.Draw(image)

    for i in range(8):
        count = 0

        for j in range(8):
            if random() < 0.5 and count < 3:
                draw.rectangle((i * 32, j * 32, i * 32 + 32,
                               j * 32 + 32), fill='#ffffff')

                count += 1

    timestamp = datetime.timestamp(datetime.now())

    image.save(f'./icons/{timestamp}.png')

    return f'./icons/{timestamp}.png'


if __name__ == '__main__':
    generate_icon()
