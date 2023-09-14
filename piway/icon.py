from PIL import Image, ImageDraw
from random import random
from datetime import datetime
from os import listdir, mkdir

from theme import colors


def generate_icon():
    image = Image.new('RGB', (256, 256), colors['primary'])
    draw = ImageDraw.Draw(image)

    for i in range(8):
        count = 0

        for j in range(8):
            if random() < 0.5 and count < 3:
                draw.rectangle((i * 32, j * 32, i * 32 + 32,
                               j * 32 + 32), fill=colors['secondary'])

                count += 1

    if 'icons' not in listdir('./piway/assets'):
        mkdir('./piway/assets/icons')

    filename = f'./piway/assets/icons/{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.png'

    image.save(filename)

    return filename


if __name__ == '__main__':
    generate_icon()
