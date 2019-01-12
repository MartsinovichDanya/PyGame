import pygame
from board import Board
import numpy as np


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


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
board = Life(8, 8)
board.set_view(40, 40, 50)
while True:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONDOWN:
        board.get_click(pygame.event.wait().pos)
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        board.fix()
    elif event.type == pygame.QUIT:
        break
    screen.fill((0, 0, 0))
    if board.population is not None:
        board.next_move()
    board.render(screen)
    pygame.display.flip()
pygame.quit()
