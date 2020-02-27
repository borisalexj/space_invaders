import pygame
import random
import math

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('../assets/img/background/background1.png')

# Caption and Icon
pygame.display.set_caption("eKids project")
icon = pygame.image.load('../assets/img/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('../assets/img/player/player1.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('../assets/img/enemy/enemy0.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

# Sound
fireSound = pygame.mixer.Sound('../assets/sound/laser.wav')

# Bullet
bulletImg = pygame.image.load('../assets/img/bullet/bullet1.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def draw_player(x, y):
    screen.blit(playerImg, (x, y))

def draw_enemy(x, y):
    screen.blit(enemyImg, (x, y))

def draw_fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Timer
clock = pygame.time.Clock()

# Game Loop
running = True
while running:

    clock.tick(50)

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_SPACE:
                # if bullet_state is "ready":
                # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    draw_fire_bullet(bulletX, bulletY)
                    fireSound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        draw_fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX  += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX  >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    draw_enemy(enemyX, enemyY)

    draw_player(playerX, playerY)
    pygame.display.update()
