# cell.py

import pygame
from solver import valid, backtrack

pygame.font.init()

class Cell:

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        self.temp = 0

    
    def draw(self, screen):
        font = pygame.font.SysFont("Tahoma", 40)
        gap = self.width / 9
        x, y = self.col * gap, self.row * gap
        if self.value == 0 and self.temp != 0:
            text = font.render(str(self.temp), 1, (128, 128, 128))
            screen.blit(text, (x + 5, y + 5))
        elif self.value != 0:
            text = font.render(str(self.value), 1, (0, 0, 0))
            screen.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, gap, gap), 3)
    

    def set_value(self, value):
        self.value = value

    
    def set_temp(self, temp):
        self.temp = temp


