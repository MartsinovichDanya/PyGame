import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    # image = image.convert_alpha()
    if colorkey is not None:
        image = image.convert()
        if colorkey is -1:
            colorkey = image.get_at((1, 1))
        image.set_colorkey(colorkey)
    return image


class Ball:
    def __init__(self, pos, r=10, color=pygame.Color('white')):
        self.x = pos[0]
        self.y = pos[1]
        self.vx = 100
        self.vy = 0
        self.r = r
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def update(self, tick):
        self.x += int(self.vx * tick / 1000)
        self.y += int(self.vy * tick / 1000)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


size = width, height = 700, 700
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
bg = Background('background.jpg', [0, 0])


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


wizard = AnimatedSprite(load_image("sorlosheet.png", (128, 128, 128, 255)), 4, 1, 66, 72)

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        wizard.rect.x += 3
        wizard.update()
    if keys[pygame.K_LEFT]:
        wizard.rect.x -= 3
        wizard.update()
    if keys[pygame.K_UP]:
        wizard.rect.y -= 3
        wizard.update()
    if keys[pygame.K_DOWN]:
        wizard.rect.y += 3
        wizard.update()
    screen.blit(bg.image, bg.rect)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
