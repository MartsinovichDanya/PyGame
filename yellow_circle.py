import pygame


class Ball:
    def __init__(self, pos, r=1, color=pygame.Color('yellow')):
        self.pos = pos
        self.r = r
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.r)


pygame.init()
uinput = [int(el) for el in input().split()]
size = width, height = uinput[0], uinput[1]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
ball = None
running = True
while running:
    tick = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball = Ball(event.pos)
    screen.fill((0, 0, 255))
    if ball:
        ball.r += int(10 * tick / 100)
        ball.draw()
    pygame.display.flip()
