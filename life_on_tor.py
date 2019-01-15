import pygame
from board import Board
import numpy as np
from time import sleep


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.population = None
    def fix(self):
        self.population = np.array(self.board, dtype=np.uint8)

    def next_move(self):
        neighbors = sum([
            np.roll(np.roll(self.population, -1, 1), 1, 0),
            np.roll(np.roll(self.population, 1, 1), -1, 0),
            np.roll(np.roll(self.population, 1, 1), 1, 0),
            np.roll(np.roll(self.population, -1, 1), -1, 0),
            np.roll(self.population, 1, 1),
            np.roll(self.population, -1, 1),
            np.roll(self.population, 1, 0),
            np.roll(self.population, -1, 0)
        ])
        self.board = (neighbors == 3) | (self.population & (neighbors == 2))
        self.population = self.board


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
board = Life(8, 8)
board.set_view(40, 40, 50)
running = True
start_live = False
pause = 0.6
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_live = not start_live
            if board.population is None:
                board.fix()
        if start_live:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    pause += 0.15
                else:
                    pause -= 0.15
                    if pause < 0:
                        pause = 0
            continue
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    if start_live:
        board.next_move()
        sleep(pause)
    board.render(screen)
    pygame.display.flip()
