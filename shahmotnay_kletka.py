import pygame


def draw_rect(n):
    screen.fill((0, 0, 0))
    x, y = 0, 0
    w, h = width // n, width // n
    for i in range(n):
        x = 0
        for j in range(n):
            if not (i + j) % 2:
                pygame.draw.rect(screen, (255, 255, 255), (x, y, w, h))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, w, h))
            x += w
        y += h


pygame.init()
uinput = [int(el) for el in input().split()]
size = width, height = uinput[0], uinput[0]
n = uinput[1]
screen = pygame.display.set_mode(size)
draw_rect(n)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
