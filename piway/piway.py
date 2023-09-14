import numpy as np
import pygame
from time import sleep

from theme import colors


class Piway:
    def __init__(self, screen, screen_width, screen_height, generation_timeout=0.1):
        self.screen = screen

        # 24px per cell
        self.columns = screen_width // 24
        self.rows = int(screen_height *
                        0.9) // 24  # 90% of screen height

        self.matrix = np.ndarray(shape=(self.columns, self.rows), dtype=int)

        for y in range(self.rows):
            for x in range(self.columns):
                self.matrix[x, y] = 0

        self.alive_cells = 0
        self.dead_cells = 0
        self.cell_count = 0
        self.generation = 0

        self.generation_timeout = generation_timeout

        self.paused = True

    def compute_next_generation(self):
        self.screen.fill(colors['primary'])

        for y in range(self.rows):
            for x in range(self.columns):
                if self.matrix[x, y] == 1:
                    pygame.draw.rect(self.screen, colors['secondary'],
                                     (x * 24, y * 24, 24, 24))

                else:
                    pygame.draw.rect(self.screen, colors['shade'],
                                     (x * 24, y * 24, 24, 24), 1)

        if not self.paused:
            next_generation_matrix = np.ndarray(
                shape=(self.columns, self.rows), dtype=int)

            for y in range(self.rows):
                for x in range(self.columns):
                    cell = self.matrix[x, y]
                    neighbors = self.get_cell_neighbors(x, y)

                    if cell == 0 and neighbors == 3:
                        next_generation_matrix[x, y] = 1

                        self.alive_cells += 1
                        self.cell_count += 1

                    elif cell == 1 and (neighbors < 2 or neighbors > 3):
                        next_generation_matrix[x, y] = 0

                        self.alive_cells -= 1
                        self.dead_cells += 1

                    else:
                        next_generation_matrix[x, y] = cell

            self.matrix = next_generation_matrix
            self.generation += 1

        sleep(self.generation_timeout)

    def get_cell_neighbors(self, x, y):
        neighbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                x_edge = (x + i + self.columns) % self.columns
                y_edge = (y + j + self.rows) % self.rows

                neighbors += self.matrix[x_edge, y_edge]

        neighbors -= self.matrix[x, y]

        return neighbors

    def handle_click(self, x, y):
        scaled_x = x // 24
        scaled_y = y // 24

        if scaled_x >= self.columns or scaled_y >= self.rows:
            pass

        elif self.matrix[scaled_x, scaled_y] == 0:
            self.matrix[scaled_x, scaled_y] = 1

            self.alive_cells += 1
            self.cell_count += 1

        else:
            self.matrix[scaled_x, scaled_y] = 0

            self.alive_cells -= 1
            self.dead_cells += 1

    def restart(self):
        self.matrix = np.ndarray(shape=(self.columns, self.rows), dtype=int)

        for y in range(self.rows):
            for x in range(self.columns):
                self.matrix[x, y] = 0

        self.alive_cells = 0
        self.dead_cells = 0
        self.cell_count = 0
        self.generation = 0

        self.paused = True
