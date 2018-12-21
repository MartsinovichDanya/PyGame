import pygame


def draw_cross():
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, height), (width, 0), 5)


pygame.init()
uinput = [int(el) for el in input().split()]
size = width, height = uinput[0], uinput[1]
screen = pygame.display.set_mode(size)
draw_cross()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
