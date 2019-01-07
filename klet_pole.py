import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
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
        if self.board[y][x] == 2:
            self.board[y][x] = 0
        else:
            self.board[y][x] += 1

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
                    pygame.draw.rect(screen, (255, 255, 255), rect, 1)
                elif self.board[i][j] == 1:
                    pygame.draw.rect(screen, (255, 0, 0), rect)
                    pygame.draw.rect(screen, (255, 255, 255), rect, 1)
                elif self.board[i][j] == 2:
                    pygame.draw.rect(screen, (0, 0, 255), rect)
                    pygame.draw.rect(screen, (255, 255, 255), rect, 1)


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
board = Board(8, 9)
board.set_view(50, 50, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
