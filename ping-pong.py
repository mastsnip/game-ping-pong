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
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < H-100:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < H-100:
            self.rect.y += self.speed



W, H = 700, 500
window = display.set_mode((W, H))
BACKGROUND = (66,170,255)
window.fill(BACKGROUND)
display.set_caption("Пинг Понг")

clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 10, H//2, 25, 100, 10)
racket2 = Player('racket.png', W-35, H//2, 25, 100, 10)
ball = GameSprite('ball.png', W//2, H//2, 50, 50, 0)

font.init()
font = font.Font(None, 35)
lose1 = font.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose2 = font.render("PLAYER 2 LOSE!", True, (180, 0, 0))
restart_game = font.render("PRESS SPACE FOR RESTART GAME!", True, (0, 0, 0))

speed_x = 3
speed_y = 3

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.fill(BACKGROUND)


        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > H-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > W:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()

        racket1.update_l()
        racket2.update_r()

    else:
        window.blit(restart_game, (0, 0))
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:
            game = True
            

    display.update()
    clock.tick(FPS)
