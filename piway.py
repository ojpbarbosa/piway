import pygame

from icons.generator import generate_icon

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption('Piway\'s Game of Life')
pygame.display.set_icon(pygame.image.load(generate_icon()))


def piway():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    piway()
