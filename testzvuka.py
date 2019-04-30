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
        self.population = self.board


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
board = Life(8, 8)
board.set_view(40, 40, 50)
running = True
start_live = False
clock = pygame.time.Clock()
fps = 5
pygame.mixer.init()
pygame.mixer.music.load(('test' + '.wav'))
volume = 10
loop = 1
rewind = 1
pygame.mixer.music.set_volume(volume/100)
pygame.mixer.music.play(-loop)

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
                if event.button == 4:
                    fps += 1
                else:
                    fps -= 1
                    if fps < 1:
                        fps = 1
            continue
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    if start_live:
        clock.tick(fps)
        board.next_move()
    board.render(screen)
    pygame.display.flip()
