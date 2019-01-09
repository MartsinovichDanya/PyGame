import pygame
from random import randint


class Board:

    def fill(self, width, height):
        self.board = [[0] * width for _ in range(height)]
        for i in range(width * height // 2):
            x = randint(0, width - 1)
            y = randint(0, height - 1)
            while self.board[y][x] == 1:
                x = randint(0, width - 1)
                y = randint(0, height - 1)
            self.board[y][x] = 1

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.counter = 1
        self.fill(width, height)
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if (x < self.left or x > self.left + self.cell_size * self.width) or \
           (y < self.top or y > self.top + self.cell_size * self.height):
            return None
        else:
            res_x = (x - self.left) // self.cell_size
            res_y = (y - self.top) // self.cell_size
            return res_x, res_y

    def on_click(self, cell_coords):
        x, y = cell_coords
        for i in range(self.height):
            for j in range(self.width):
                if (i == y or j == x) and self.board[i][j] != bool(self.counter % 2):
                    self.board[i][j] = int(not self.board[i][j])
        self.counter += 1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                rect = (self.left + self.cell_size * j,
                        self.top + self.cell_size * i,
                        self.cell_size,
                        self.cell_size)
                if self.board[i][j] == 0:
                    color = (0, 0, 255)
                else:
                    color = (255, 0, 0)
                pygame.draw.circle(screen, color,
                                   (rect[0] + self.cell_size // 2,
                                    rect[1] + self.cell_size // 2),
                                   self.cell_size // 2 - 4)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
board = Board(8, 8)
board.set_view(40, 40, 50)
while True:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONDOWN:
        board.get_click(pygame.event.wait().pos)
    elif event.type == pygame.QUIT:
        break
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()
