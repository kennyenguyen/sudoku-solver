# GUI.py

import pygame
import time
from solver import valid, backtrack
from grid import Grid
from cell import Cell

pygame.font.init()

def redraw_window(screen, board, time, strikes):
    screen.fill((255, 255, 255))
    # draw time
    font = pygame.font.SysFont("Tahoma", 40)
    text = font.render("Time: " + format_time(time), 1, (0, 0, 0))
    screen.blit(text, (540 - 160, 560))
    # draw strikes
    text = font.render("X " * strikes, 1, (255, 0, 0))
    screen.blit(text, (20, 560))
    # draw grid
    board.draw(screen)


def format_time(time):
    seconds = time % 60
    minutes = time // 60
    return " " + str(minutes).rjust(2, "0") + ":" + str(seconds).rjust(2, "0")


def main():
    screen = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    key = None
    running = True
    start_time = time.time()
    strikes = 0

    while running:
        time_elapsed = round(time.time() - start_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_BACKSPACE:
                    board.clear()
                    key = None
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    row, col = board.selected
                    if board.cells[row][col].temp != 0:
                        if not board.place(board.cells[row][col].temp):
                            strikes += 1
                        key = None
                        if board.is_finished():
                            running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(screen, board, time_elapsed, strikes)
        pygame.display.update()


main()
pygame.quit()


