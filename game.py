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
isRedMax = False


y = 0



while running:
 # Держим цикл на правильной скорости 
    clock.tick(FPS)
    screen.fill((red, green, blue))
    # green = green + 1

    if isRedMax == True:
        green = green + 1
    else:
         red = red + 1
         if red == 255:
          red = 0
          isRedMax = True
    print(red)
    


    pygame.draw.rect(screen,(100,50,200),[0,y,100,200])  
    y = y +0.1

        #Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.display.flip()
    
    
  


pygame.quit()