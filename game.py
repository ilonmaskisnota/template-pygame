import pygame
 
WIDTH = 360
HEIGHT =  480
FPS = 30
# Задаём цвета 
WHITE =  (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
BLUE = (0, 0, 255)
 # Создаём игру в окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game pro")
clock = pygame.time.Clock()
# Цикл игры
running = True
red = 0 
green = 0 
blue = 0 
while running:
 # Держим цикл на правильной скорости 
    clock.tick(FPS)
    screen.fill((red, green, blue))
    green = green + 1
    red = red + 1
    if green == 255:
        green = 0
    if red == 255:
        red = 0
        #Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.display.flip()


pygame.quit()