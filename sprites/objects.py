import pygame


class Sprite:
    X_change = 0
    Y_change = 10

    def __init__(self, screen_driver, sprite):
        self.screen = screen_driver
        self.sprite = sprite

    def blit(self, *args):
        self.screen.blit(self.sprite, *args)


class Bullet(Sprite):
    prepared = True
    x, y = (0, 480)

    def move(self):
        self.prepared = False
        self.blit((self.x + 16, self.y + 10), )

    def try_reload_bullet(self):
        if self.y <= 0:
            self.y = 480
            self.prepared = True

    def check_collision(self, enemy):
        rect = self.sprite.get_rect()
        enemy_rect = enemy.sprite.get_rect()
        return pygame.sprite.collide_rect(rect, enemy_rect)


class Player(Sprite):
    x, y = (370, 480)

    def move(self):
        self.blit((self.x, self.y), )


class Enemy(Sprite):
    x, y = (0, 0)

    def move(self):
        self.blit((self.x, self.y), )