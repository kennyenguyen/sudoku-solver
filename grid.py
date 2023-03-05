# grid.py

import pygame
from solver import valid, backtrack
from cell import Cell

class Grid:

    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.cells = [[Cell(self.board[row][col], row, col, width, height) for col in range(cols)] for row in range(rows)]
        self.model = None
        self.selected = None

    
    def update_model(self):
        self.model = [[self.cells[row][col].value for col in range(self.cols)] for row in range(self.rows)]
        

    def place(self, value):
        row, col = self.selected
        if self.cells[row][col].value == 0:
            self.cells[row][col].set_value(value)
            self.update_model()
            if valid(self.model, value, row, col) and backtrack(self.model):
                return True
            else:
                self.cells[row][col].set_value(0)
                self.cells[row][col].set_temp(0)
                self.update_model()
                return False
        

    def sketch(self, value):
        row, col = self.selected
        self.cells[row][col].set_temp(value)
        

    def draw(self, screen):
        # draw grid lines
        gap = self.width / 9
        for row in range(self.rows + 1):
            if row % 3 == 0 and row != 0:
                thick = 4
            else:
                thick = 1
            # horizontal lines
            pygame.draw.line(screen, (0, 0, 0), (0, row * gap), (self.width, row * gap), thick)
            # vertical lines
            pygame.draw.line(screen, (0, 0, 0), (row * gap, 0), (row * gap, self.height), thick)
        # draw cells
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col].draw(screen)
        

    def select(self, row, col):
        # unselect all cells
        for r in range(self.rows):
            for c in range(self.cols):
                self.cells[r][c].selected = False
        # select (row, col)
        self.cells[row][col].selected = True
        self.selected = (row, col)
        

    def clear(self):
        row, col = self.selected
        if self.cells[row][col].value == 0:
            self.cells[row][col].set_temp(0)
        

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))
        else:
            return None
        

    def is_finished(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col].value == 0:
                    return False
        return True
        

