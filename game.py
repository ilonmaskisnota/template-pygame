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
x = 0

colorApple = (255,150,100)
x_apple = 100
y_apple = 200

while running:
 # Держим цикл на правильной скорости 
    clock.tick(FPS)
    screen.fill((red, green, blue))
  
    

    pygame.draw.rect(screen,(100,50,200),[x,y,100,200])  
    #яблоко рисуем
    pygame.draw.circle(screen, colorApple, [x_apple,y_apple],15)


    #Проверка нажатия на клавишы движения
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            print("quit")
            running = False
        #если нажали на кнопку на клавиатуре
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("нажали на w")
                y = y - 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("нажали на a")    
                x = x - 10 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print("нажали на s")  
                y = y + 10 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print("нажали на d")   
                x = x + 10

    pygame.display.flip()
pygame.quit()
