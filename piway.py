import pygame

from icon import generate
from theme import colors

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption('Piway\'s Game of Life')
pygame.display.set_icon(pygame.image.load(generate()))


def piway():
    running = True

    while running:
        clock.tick(60)
        screen.fill(colors['primary'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    piway()
