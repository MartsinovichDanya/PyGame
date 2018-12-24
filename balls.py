import pygame


class Ball:
    def __init__(self, pos, r=10, color=pygame.Color('white')):
        self.x = pos[0]
        self.y = pos[1]
        self.vx = -100
        self.vy = -100
        self.r = r
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def update(self, tick):
        self.x += int(self.vx * tick / 1000)
        self.y += int(self.vy * tick / 1000)


pygame.init()
uinput = [int(el) for el in input().split()]
size = width, height = uinput[0], uinput[1]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
balls = []
running = True
while running:
    tick = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                balls.append(Ball(event.pos))
    screen.fill((0, 0, 0))
    if balls:
        for ball in balls:
            ball.update(tick)
            if ball.y - 10 <= 0:
                ball.vy = 100
            elif ball.y + 10 >= height:
                ball.vy = -100
            if ball.x - 10 <= 0:
                ball.vx = 100
            elif ball.x + 10 >= width:
                ball.vx = -100
            ball.draw()
    pygame.display.flip()
