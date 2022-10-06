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
        self.columns = root.winfo_screenwidth() // 32  # 32px per cell
        self.rows = int(root.winfo_screenheight() *
                        0.8) // 32  # 80% of screen height

        self.world = numpy.ndarray(shape=(self.columns, self.rows), dtype=int)

        for y in range(self.rows):
            for x in range(self.columns):
                self.world[x, y] = 0

    def update(self, paused):
        self.screen.fill(colors['primary'])

        for y in range(self.rows):
            for x in range(self.columns):
                if self.world[x, y] == 1:
                    pygame.draw.rect(self.screen, colors['secondary'],
                                     (x * 32, y * 32, 32, 32))

        if not paused:
          updated_world = numpy.ndarray(
            shape=(self.columns, self.rows), dtype=int)

          for y in range(self.rows):
              for x in range(self.columns):
                  cell = self.world[x, y]
                  neighbors = self.get_neighbors(x, y)

                  if cell == 0 and neighbors == 3:
                      updated_world[x, y] = 1

                  elif cell == 1 and (neighbors < 2 or neighbors > 3):
                      updated_world[x, y] = 0

                  else:
                      updated_world[x, y] = cell

          self.world = updated_world

        sleep(0.1)

    def get_neighbors(self, x, y):
        neighbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                x_edge = (x + i + self.columns) % self.columns
                y_edge = (y + j + self.rows) % self.rows

                neighbors += self.world[x_edge, y_edge]

        neighbors -= self.world[x, y]

        return neighbors

    def click(self, x, y):
        x_scaled = x // 32
        y_scaled = y // 32

        if self.world[x_scaled, y_scaled] == 0:
            self.world[x_scaled, y_scaled] = 1

        else:
            self.world[x_scaled, y_scaled] = 0


if __name__ == '__main__':
    Conway()
