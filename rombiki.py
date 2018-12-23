import pygame


def draw_romb(n):
    screen.fill(pygame.Color('yellow'))
    for i in range(width // n):
        for j in range(height // n):
            tochki = [(n // 2 + n * j, n * i),
                      (n * j, n // 2 + n * i),
                      (n // 2 + n * j, n * (i + 1)),
                      (n * (j + 1), n // 2 + n * i)]
            pygame.draw.polygon(screen, pygame.Color('orange'), tochki)


pygame.init()
n = int(input())
size = width, height = 155, 155
screen = pygame.display.set_mode(size)
draw_romb(n)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
