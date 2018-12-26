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

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(self, cell)

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                rect = (self.left + self.cell_size * j,
                        self.top + self.cell_size * i,
                        self.cell_size,
                        self.cell_size)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
board = Board(4, 3)
board.set_view(100, 100, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
