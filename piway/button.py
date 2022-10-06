# https://www.youtube.com/watch?v=4_9twnEduFA
import pygame


class Button:
    def __init__(self, screen, color, x, y, width, height, text):
        self.screen = screen

        self.color = color

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.text = text

        self.font = pygame.font.Font('./fonts/emulogic.ttf', 60)

    def draw(self, outline=None):
        if outline:
            pygame.draw.rect(self.screen, outline, (self.x - 2,
                             self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(self.screen, self.color,
                         (self.x, self.y, self.width, self.height), 0)

        text = self.font.render(self.text, 1, (0, 0, 0))

        self.screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                         self.y + (self.height / 2 - text.get_height() / 2)))

    def hovering(self, x, y):
        if x > self.x and x < self.x + self.width:
            if y > self.y and y < self.y + self.height:
                return True

        return False
