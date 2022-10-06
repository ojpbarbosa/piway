import tkinter
import numpy
import pygame
from theme import colors
from time import sleep


class Conway:
    def __init__(self, screen):
        self.screen = screen

        self.world = []

        root = tkinter.Tk()
        self.columns = root.winfo_screenwidth() // 24 # 24px per cell
        # self.rows = int(root.winfo_screenheight() *
        #                 0.9) // 24 # 90% of screen height
        self.rows = root.winfo_screenheight() // 24

        self.world = numpy.ndarray(shape=(self.columns, self.rows), dtype=int)

        for y in range(self.rows):
            for x in range(self.columns):
                self.world[x, y] = 0

        self.alive_cells = 0
        self.dead_cells = 0
        self.cell_count = 0
        self.generation = 0

        self.paused = False

    def compute_next_generation(self):
        self.screen.fill(colors['primary'])

        for y in range(self.rows):
            for x in range(self.columns):
                if self.world[x, y] == 1:
                    pygame.draw.rect(self.screen, colors['secondary'],
                                     (x * 24, y * 24, 24, 24))
                            

                else:
                    pygame.draw.rect(self.screen, colors['shade'],
                                     (x * 24, y * 24, 24, 24), 1)

        if not self.paused:
          next_generation_world = numpy.ndarray(
            shape=(self.columns, self.rows), dtype=int)

          for y in range(self.rows):
              for x in range(self.columns):
                  cell = self.world[x, y]
                  neighbors = self.get_cell_neighbors(x, y)

                  if cell == 0 and neighbors == 3:
                      next_generation_world[x, y] = 1
                      
                      self.alive_cells += 1
                      self.cell_count += 1

                  elif cell == 1 and (neighbors < 2 or neighbors > 3):
                      next_generation_world[x, y] = 0

                      self.alive_cells -= 1
                      self.dead_cells += 1

                  else:
                      next_generation_world[x, y] = cell

          self.world = next_generation_world
          self.generation += 1


        sleep(0.1)

    def get_cell_neighbors(self, x, y):
        neighbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                x_edge = (x + i + self.columns) % self.columns
                y_edge = (y + j + self.rows) % self.rows

                neighbors += self.world[x_edge, y_edge]

        neighbors -= self.world[x, y]

        return neighbors

    def handle_click(self, x, y):
        x_scaled = x // 24
        y_scaled = y // 24

        if x_scaled >= self.columns or y_scaled >= self.rows:
            pass

        elif self.world[x_scaled, y_scaled] == 0:
            self.world[x_scaled, y_scaled] = 1

            self.alive_cells += 1
            self.cell_count += 1

        else:
            self.world[x_scaled, y_scaled] = 0


if __name__ == '__main__':
    Conway()