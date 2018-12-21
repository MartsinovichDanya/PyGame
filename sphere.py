import pygame


def draw_sphere(n):
    screen.fill((0, 0, 0))
    step = 150 // n
    for i in range(n):
        rect = (0, 0 + step * i, 300, 300 - step * 2 * i)
        pygame.draw.ellipse(screen, (255, 255, 255), rect, 1)
    for i in range(n):
        rect = (0 + step * i, 0, 300 - step * 2 * i, 300)
        pygame.draw.ellipse(screen, (255, 255, 255), rect, 2)


pygame.init()
n = int(input())
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
draw_sphere(n)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
