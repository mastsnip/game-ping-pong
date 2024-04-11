from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_S] and self.rect.y < H:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < H:
            self.rect.y += self.speed



W, H = 700, 700
window = display.set_mode((W, H))
BACKGROUND = (66,170,255)
window.fill(BACKGROUND)
display.set_caption("Пинг Понг")

clock = time.Clock()
FPS = 60

racket1 = Player('racket1.png', 10, H//2, 50, 200, 10)
racket2 = Player('racket2.png', W-10, H//2, 50, 200, 10)
ball = GameSprite('ball.png', W//2, H//2, 50, 50, 15)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
