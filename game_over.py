import pygame

from background import Background

pygame.init()

size = width, height = 600, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('blue'))
bg = Background('gameover.jpg', [0, 0])

running = True
clock = pygame.time.Clock()
x = -600

while running:
    tick = clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if x != 0:
        x += 10
    bg = Background('gameover.jpg', [x, 0])
    screen.blit(bg.image, bg.rect)
    pygame.display.flip()
