import pygame

from icon import generate_icon
from theme import colors
from piway import Piway
from button import Button
from utilities import human_format


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_window_size()

    pygame.display.set_caption('Piway\'s Game of Life')
    pygame.display.set_icon(pygame.image.load(generate_icon()))

    piway = Piway(screen, SCREEN_WIDTH, SCREEN_HEIGHT, 0.15)

    BUTTON_WIDTH = 240
    BUTTON_HEIGHT = 60

    MARGIN = 15

    quit_button_x = SCREEN_WIDTH - MARGIN - BUTTON_WIDTH
    button_y = SCREEN_HEIGHT - 82.5

    quit_button = Button(
        screen, colors['secondary'], colors['primary'], quit_button_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT, 'quit')

    restart_button = Button(
        screen, colors['secondary'], colors['primary'], quit_button_x - BUTTON_WIDTH - MARGIN, button_y, BUTTON_WIDTH, BUTTON_HEIGHT, 'restart')

    pause_button = Button(
        screen, colors['secondary'], colors['primary'], restart_button.x - BUTTON_WIDTH - MARGIN, button_y, BUTTON_WIDTH, BUTTON_HEIGHT, 'pause')

    gosper_glider_gun_button = Button(
        screen, colors['secondary'], colors['primary'], pause_button.x - BUTTON_WIDTH - MARGIN, button_y, BUTTON_WIDTH, BUTTON_HEIGHT, 'ggg')

    running = True

    font = pygame.font.Font('./piway/assets/fonts/emulogic.ttf', 24)

    while running:
        screen.fill(colors['primary'])
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                    piway.paused = not piway.paused

                elif event.key == pygame.K_q:
                    running = False

                elif event.key == pygame.K_r:
                    piway.restart()

                elif event.key == pygame.K_g:
                    piway.load_matrix_from_file('gosper_glider_gun')

        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()

            piway.handle_click(x, y)

            if restart_button.is_hovering(x, y):
                piway.restart()

            elif quit_button.is_hovering(x, y):
                running = False

            elif pause_button.is_hovering(x, y):
                piway.paused = not piway.paused

            elif gosper_glider_gun_button.is_hovering(x, y):
                piway.load_matrix_from_file('gosper_glider_gun')

        piway.compute_next_generation()

        screen.blit(font.render(
            'cells: ' + human_format(piway.cell_count), 1, colors['secondary']), (MARGIN,
                                                                                  SCREEN_HEIGHT - 100
                                                                                  ))

        screen.blit(font.render(
            'alive cells: ' + human_format(piway.alive_cells), 1, colors['secondary']), (MARGIN,
                                                                                         SCREEN_HEIGHT - 70
                                                                                         ))

        screen.blit(font.render(
            'dead cells: ' + human_format(piway.dead_cells), 1, colors['secondary']), (MARGIN,
                                                                                       SCREEN_HEIGHT - 40
                                                                                       ))

        x, y = pygame.mouse.get_pos()

        restart_button.draw()
        quit_button.draw()

        pause_button.text = 'play' if piway.paused else 'pause'
        pause_button.draw()

        gosper_glider_gun_button.draw()

        if restart_button.is_hovering(x, y):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            restart_button.draw_hovering()
        elif quit_button.is_hovering(x, y):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            quit_button.draw_hovering()
        elif pause_button.is_hovering(x, y):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            pause_button.draw_hovering()
        elif gosper_glider_gun_button.is_hovering(x, y):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            gosper_glider_gun_button.draw_hovering()
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
