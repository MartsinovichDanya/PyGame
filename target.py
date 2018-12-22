import pygame


def draw_targ(n, kol):
    screen.fill((0, 0, 0))
    centre = (width // 2, height // 2)
    for i in range(kol):
        if not (i + 1) % 3:
            pygame.draw.circle(screen, (0, 0, 255), centre, n*(i + 1), n)
        elif (i + 1) % 3 == 2:
            pygame.draw.circle(screen, (0, 255, 0), centre, n*(i + 1), n)
        else:
            pygame.draw.circle(screen, (255, 0, 0), centre, n*(i + 1), n)

pygame.init()
uinput = [int(el) for el in input().split()]
n = uinput[0]
k = uinput[1]
size = width, height = n*k*2, n*k*2
screen = pygame.display.set_mode(size)
draw_targ(n, k)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
