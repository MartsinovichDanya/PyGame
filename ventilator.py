import pygame
import math


def turn(angle):
    x2 = int(101 + 70 * math.cos(math.radians(angle)))
    y2 = int(101 + 70 * math.sin(math.radians(angle)))
    return x2, y2

class Blade:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def draw(self):
        pygame.draw.polygon(screen, pygame.Color('white'), [self.p1, self.p2, self.p3])


pygame.init()
size = width, height = 201, 201
screen = pygame.display.set_mode(size)
pygame.draw.circle(screen, pygame.Color('white'), (101, 101), 10)
blade1 = Blade((101, 101), (118, 33), (84, 33))
blade1.draw()
blade2 = Blade((101, 101), turn(105), turn(75))
blade2.draw()
blade3 = Blade((101, 101), turn(315), turn(285))
blade3.draw()
pygame.display.flip()
clock = pygame.time.Clock()
running = True
while running:
    tick = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass
    # screen.fill((0, 0, 0))

    pygame.display.flip()
