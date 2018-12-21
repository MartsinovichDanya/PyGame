import pygame


def draw_rect():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (1, 1, width - 2, height - 2))


pygame.init()
uinput = [int(el) for el in input().split()]
size = width, height = uinput[0], uinput[1]
screen = pygame.display.set_mode(size)
draw_rect()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
