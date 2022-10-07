from PIL import Image, ImageDraw
from random import random
from datetime import datetime
from os import listdir, mkdir

from theme import colors


def generate():
    image = Image.new('RGB', (256, 256), colors['primary'])
    draw = ImageDraw.Draw(image)

    for i in range(8):
        count = 0

        for j in range(8):
            if random() < 0.5 and count < 3:
                draw.rectangle((i * 32, j * 32, i * 32 + 32,
                               j * 32 + 32), fill=colors['secondary'])

                count += 1

    timestamp = datetime.timestamp(datetime.now())

    if 'icons' not in listdir():
        mkdir('icons')

    image.save(f'./icons/{timestamp}.png')

    return f'./icons/{timestamp}.png'


if __name__ == '__main__':
    generate()
