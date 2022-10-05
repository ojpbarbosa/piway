import pygame

from icon import generate

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()

pygame.display.set_caption('Piway\'s Game of Life')
pygame.display.set_icon(pygame.image.load(generate()))


def piway():
    running = True

    while running:
        screen.fill((255, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    piway()
