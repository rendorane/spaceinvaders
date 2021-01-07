import pygame
import random
import math

pygame.init()
width = 1000
height = 800
win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Dinopunk 2077 mln years ago")
icon = pygame.image.load("crux.png")
pygame.display.set_icon(icon)

playerIcon = pygame.image.load("chef.png")
playerSize = playerIcon.get_size()
playerX, playerY = width / 2 - playerSize[0] / 2, height - 100
playerMoveX = 0

enemies_number = 10
enemyIcon = pygame.image.load("bactrosaurus.png")
enemySize = enemyIcon.get_size()
enemyMoveX = []
enemyMoveY = []
enemyX = []
enemyY = []

for i in range(enemies_number):
    enemyX.append(random.randint(0, width - enemySize[0]))
    enemyY.append(random.randint(50, 150))
    enemyMoveX.append(2)
    enemyMoveY.append(50)

bullets_number = 10
bulletIcon = pygame.image.load("eggs.png")
bulletSize = bulletIcon.get_size()

bulletX = []
bulletY = []
bulletMoveY = []
bulletState = []

for i in range(bullets_number):
    bulletX.append(0)
    bulletY.append(playerY)
    bulletMoveY.append(5)
    bulletState.append("rdy")

# bulletX, bulletY = 0, playerY
# bulletMoveY = 5
# bulletState = 'rdy'

deadIcon = pygame.image.load("surprise.png")

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

game_over_font = pygame.font.Font('freesansbold.ttf', 128)

starsList = []

for i in range(100):
    starsList.append((random.randint(0, width), random.randint(0, height)))


def enemy(x, y, i):
    win.blit(enemyIcon, (x[i], y[i]))


def player(x, y):
    win.blit(playerIcon, (x, y))


def bullet(x, y, i):
    global bulletState
    bulletState[i] = 'fired'
    win.blit(bulletIcon, (x[i] + playerSize[0] / 2 - bulletSize[0] / 2, y[i] - bulletSize[1]))


def deadPlayer(x, y):
    win.blit(deadIcon, (x, y))


def isCollision(bulletX, bulletY, enemyX, enemyY):
    d = math.sqrt((math.pow((bulletX + bulletSize[0] / 2) - (enemyX + enemySize[0] / 2), 2))
                  + (math.pow((bulletY + bulletSize[1] / 2) - (enemyY + enemySize[1] / 2), 2)))
    if d < 40:
        return True
    else:
        return False


def show_score(x, y):
    score_show = font.render("Score: {}".format(score), True, (255, 255, 255))
    win.blit(score_show, (x, y))


def game_over_text(x, y):
    game_over_show = game_over_font.render("WASTED", True, (255,255,255))
    x_off, y_off = game_over_show.get_size()
    win.blit(game_over_show, (x - x_off/2, y - y_off/2))


isAlive = True
running = True
while running:
    win.fill((0, 0, 0))

    if isAlive:
        player(playerX, playerY)

    for star in starsList:
        pygame.draw.circle(win, (255, 255, 255), star, 1)

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerMoveX = 3
            if event.key == pygame.K_LEFT:
                playerMoveX = -3
            for i in range(bullets_number):
                if event.key == pygame.K_SPACE:
                    if bulletState[i] == "rdy":
                        bulletX[i] = playerX
                        bullet(bulletX, bulletY, i)
                        break
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerMoveX = 0
    playerX += playerMoveX
    if playerX <= 0:
        playerX = 0
    elif playerX >= width - playerSize[0]:
        playerX = width - playerSize[0]
    for i in range(bullets_number):
        if bulletState[i] == "fired":
            bullet(bulletX, bulletY, i)
            bulletY[i] -= bulletMoveY[i]
        if bulletY[i] <= 0 - bulletSize[1]:
            bulletY[i] = playerY
            bulletState[i] = "rdy"
    for i in range(enemies_number):
        enemy(enemyX, enemyY, i)
        enemyX[i] += enemyMoveX[i]
        if enemyX[i] <= 0:
            enemyMoveX[i] *= -1
            enemyY[i] += enemyMoveY[i]
        elif enemyX[i] >= width - enemySize[0]:
            enemyMoveX[i] *= -1
            enemyY[i] += enemyMoveY[i]
        for j in range(bullets_number):
            collision = isCollision(bulletX[j], bulletY[j], enemyX[i], enemyY[i])
            if collision:
                bulletY[j] = playerY
                bulletState[j] = 'rdy'
                enemyX[i] = random.randint(0, width - enemySize[0])
                enemyY[i] = random.randint(50, 150)
                score += 1
        if enemyY[i] + enemySize[1] > playerY:
            game_over_text(width / 2, height / 2)
            isAlive = False
            deadPlayer(playerX, playerY)
            for k in range(enemies_number):
                enemyMoveX[k] = 0
                enemyMoveY[k] = 0
                enemyY[k] = 1000
    show_score(10, 10)
    pygame.display.update()
