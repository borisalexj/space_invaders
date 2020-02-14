import pygame
import random
import math
from sprites import Enemy, Player, Bullet

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('assets/img/background/background1.png')
endgame_screen = pygame.image.load('assets/img/background/gameover.png')

# Caption and Icon
pygame.display.set_caption("eKids project")
pygame.display.set_icon(pygame.image.load('assets/img/ufo.png'))

clock = pygame.time.Clock()

# Enemy
num_of_enemies = 6


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    return distance < 27


def run():
    running = True
    game_over = False
    while running:
        clock.tick(50)

        if not game_over:
            screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.X_change = -5
                if event.key == pygame.K_RIGHT:
                    player.X_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet.prepared:
                        # Get the current x coordinate of the spaceship
                        bullet.x = player.x
                        bullet.move()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.X_change = 0

        player.x += player.X_change
        if player.x <= 0:
            player.x = 0
        elif player.x >= 736:
            player.x = 736

        for enemy in enemies:

            ######## Game Over ############
            if enemy.y > 440:
                game_over = True
                enemy.y = 2000
                break

            enemy.x += enemy.X_change
            if enemy.x <= 0:
                enemy.X_change = 4
                enemy.y += enemy.Y_change
            elif enemy.x >= 736:
                enemy.X_change = -4
                enemy.y += enemy.Y_change

            # Collision
            collision = isCollision(enemy.x, enemy.y, bullet.x, bullet.y)
            if collision:
                bullet.y = 480
                bullet.prepared = True
                enemy.x = random.randint(0, 736)
                enemy.y = random.randint(50, 150)

            enemy.move()

        if game_over:
            screen.blit(endgame_screen, (0, 0))

        bullet.try_reload_bullet()

        if not bullet.prepared:
            bullet.move()
            bullet.y -= bullet.Y_change

        player.move()

        pygame.display.update()


if __name__ == '__main__':
    bullet = Bullet(screen, pygame.image.load('assets/img/bullet/bullet1.png'))
    player = Player(screen, pygame.image.load('assets/img/player/player1.png'))

    enemies = []

    for i in range(num_of_enemies):
        enemy = Enemy(screen, pygame.image.load('assets/img/enemy/enemy1.png'))
        enemy.x = random.randint(0, 736)
        enemy.y = random.randint(50, 150)
        enemy.X_change = 4
        enemy.Y_change = 40
        enemies.append(enemy)

    run()
