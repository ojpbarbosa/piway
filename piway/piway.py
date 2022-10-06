import pygame

from icon import generate
from theme import colors
from conway import Conway
# import Button from button


def piway():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption('Piway\'s Game of Life')
    pygame.display.set_icon(pygame.image.load(generate()))

    conway = Conway(screen)

    # restart_button = Button(screen, colors['primary'])

    running = True

    while running:
      screen.fill(colors['primary'])
      clock.tick(60)

      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_SPACE or event.key == pygame.K_p:
                    conway.paused = not conway.paused

      if pygame.mouse.get_pressed()[0]:
          x, y = pygame.mouse.get_pos()

          conway.handle_click(x, y)

        #   if restart_button.hovering(x, y):
        #       restart_button.draw()

      conway.compute_next_generation()

      pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    piway()
