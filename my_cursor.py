import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


uinput = [int(el) for el in input().split()]
pygame.init()
size = width, height = uinput[0], uinput[1]
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
pygame.mouse.set_visible(False)
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("cursor.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)


while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    if event.type == pygame.MOUSEMOTION:
        if pygame.mouse.get_focused():
            sprite.rect.x = event.pos[0]
            sprite.rect.y = event.pos[1]
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
