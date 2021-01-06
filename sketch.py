import pygame

pygame.init()

DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

DISPLAY.fill(WHITE)

pygame.draw.rect(DISPLAY, BLUE, (200, 150, 100, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()