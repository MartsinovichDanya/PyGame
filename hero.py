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


pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("hero.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)


while True:
    event = pygame.event.wait()
    keys = pygame.key.get_pressed()
    if event.type == pygame.QUIT:
        break
    if keys[pygame.K_RIGHT]:
        sprite.rect.x += 10
    if keys[pygame.K_LEFT]:
        sprite.rect.x -= 10
    if keys[pygame.K_UP]:
        sprite.rect.y -= 10
    if keys[pygame.K_DOWN]:
        sprite.rect.y += 10
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
