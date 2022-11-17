import pygame
import tkinter as tk

from icon import generate
from theme import colors
from piway import Piway
from button import Button
from utilities import human_format


def piway():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption('Piway\'s Game of Life')
    pygame.display.set_icon(pygame.image.load(generate()))

    piway = Piway(screen)

    root = tk.Tk()

    button_x = root.winfo_screenwidth() // 2 - 120
    button_y = root.winfo_screenheight() - 82.5

    restart_button = Button(
        screen, colors['secondary'], colors['primary'], button_x, button_y, 240, 60, 'restart')

    running = True

    font = pygame.font.Font('./piway/fonts/emulogic.ttf', 24)

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
                    piway.paused = not piway.paused

        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()

            piway.handle_click(x, y)

            if restart_button.is_hovering(x, y):
                piway.restart()

        piway.compute_next_generation()

        screen.blit(font.render(
            'Cell count: ' + human_format(piway.cell_count), 1, colors['secondary']), (15,
                                                                                       root.winfo_screenheight() - 100
                                                                                       ))

        screen.blit(font.render(
            'Alive cells: ' + human_format(piway.alive_cells), 1, colors['secondary']), (15,
                                                                                         root.winfo_screenheight() - 70
                                                                                         ))

        screen.blit(font.render(
            'Dead cells: ' + human_format(piway.dead_cells), 1, colors['secondary']), (15,
                                                                                       root.winfo_screenheight() - 40
                                                                                       ))

        x, y = pygame.mouse.get_pos()
        if restart_button.is_hovering(x, y):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            restart_button.draw_hovering()
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            restart_button.draw()

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    piway()
