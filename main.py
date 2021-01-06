import pygame
import random

pygame.init()
width = 800
height = 600
win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Cyberpunk 2077")
icon = pygame.image.load("crux.png")
pygame.display.set_icon(icon)

playerIcon = pygame.image.load("jellyfish.png")
playerSize = playerIcon.get_size()
playerX, playerY = width / 2 - playerSize[0] / 2, height - 100
playerMoveX = 0

enemyIcon = pygame.image.load("lobster.png")
enemyIcon = pygame.transform.flip(enemyIcon, False, True)
enemySize = enemyIcon.get_size()
enemyX = random.randint(0, width - playerSize[0])
enemyY = random.randint(50, 150)
enemyMoveX = 1
enemyMoveY = 10

bulletIcon = pygame.image.load("sardine.png")
bulletIcon = pygame.transform.rotate(bulletIcon,90)
bulletSize = bulletIcon.get_size()
bulletX, bulletY = 0, playerY
bulletMoveY = 1
bulletState = 'rdy'

starsList = []

for i in range(100):
    starsList.append((random.randint(0, width), random.randint(0, height)))


def enemy(x, y):
    win.blit(enemyIcon, (x, y))


def player(x, y):
    win.blit(playerIcon, (x, y))


def bullet(x, y):
    global bulletState
    bulletState = 'fired'
    win.blit(bulletIcon, (x + playerSize[0] / 2 - bulletSize[0] / 2, y - bulletSize[1]))


running = True
while running:
    win.fill((0, 0, 0))
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    for star in starsList:
        pygame.draw.circle(win, (255, 255, 255), star, 1)

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerMoveX = 1
            if event.key == pygame.K_LEFT:
                playerMoveX = -1
            if event.key == pygame.K_SPACE:
                if bulletState == "rdy":
                    bulletX = playerX
                    bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerMoveX = 0
    if playerX <= 0:
        playerX = 0
    elif playerX >= width - playerSize[0]:
        playerX = width - playerSize[0]
    if enemyX <= 0:
        enemyMoveX *= -1
        enemyY += enemyMoveY
    elif enemyX >= width - enemySize[0]:
        enemyMoveX *= -1
        enemyY += enemyMoveY
    if bulletState == "fired":
        bullet(bulletX, bulletY)
        bulletY -= bulletMoveY
    if bulletY <= 0 - bulletSize[1]:
        bulletY = playerY
        bulletState = "rdy"

    playerX += playerMoveX
    enemyX += enemyMoveX


    pygame.display.update()
