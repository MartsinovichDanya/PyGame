import pygame


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

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
        self.board[y][x] = int(not self.board[y][x])

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                rect = (self.left + self.cell_size * j,
                        self.top + self.cell_size * i,
                        self.cell_size,
                        self.cell_size)
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), rect)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)



