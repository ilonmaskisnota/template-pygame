import pygame
import random
 # переменные с размерами экрана
WIDTH = 1024
HEIGHT =  600

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
#cjplftv gthtvtyye, в которую запихиваем экран,  устанавливаем ширину и высоту
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#задаю екрану название
pygame.display.set_caption("game pro")
# переменная? которая хранит время обновления экрана
clock = pygame.time.Clock()
# Цикл игры
running = True
screenColor = (0,0,0)

# параметры игрока 
y = 0
x = 0
#ширина и высота игрока
width_player = 50
height_player = 50
#цвет экрана
colorApple = (255,150,100)
#координаты яблока
x_apple = 100
y_apple = 200

#яблоко
img = pygame.image.load("./apple.png")
scale = pygame.transform.scale(img, (img.get_width()//4,img.get_height()//4))
scale_rect = scale.get_rect(center=(WIDTH/2, HEIGHT//2))

screen.blit(scale,scale_rect)
pygame.display.update()

pygame.time.wait(5000)

#змея
mino_img = pygame.image.load("./snakes.png")
scale_mino = pygame.transform.scale(mino_img, (400,200))
mino_rect = scale_mino.get_rect()
mino_rect.center = 100, 100

score = 0
score = score + 1
font_style = pygame.font.SysFont("Times New Roman", 50)
msg = font_style.render(f"Score: {score}", True, (100, 255,100),(100,40,200))

gms = font_style.render("game over", True, RED, WIDTH)


#pygame.time.wait(5000)

while running:
 # Держим цикл на правильной скорости 
    clock.tick(FPS)
    # заполнить экран цветом
    screen.fill(screenColor)
    screen.blit(scale,scale_rect)
    screen.blit(scale_mino,mino_rect)
    screen.blit(msg,[20,20])
    #рисуем прямоугольник в screen
    pygame.draw.rect(screen,(100,50,200),[x,y,width_player,height_player])  

    #яблоко рисуем
    pygame.draw.circle(screen, colorApple, [x_apple,y_apple],15)
    if (x<0 or x > WIDTH - width_player):
        running = False
        screen.blit(gms, [WIDTH//2-100,HEIGHT//2-50])
        pygame.display.flip()
        pygame.time.wait(5000)
        pass




    # столкновение с шариком
    if ((x < x_apple+15 and x_apple-15 < x + width_player ) and (y < y_apple+15 and y_apple-15 < y + height_player) ):
        width_player += 10
        x_apple = random.randint(0,WIDTH)
        y_apple = random.randint(0,HEIGHT)
        scale_rect.center = x_apple, y_apple
        pygame.draw.circle(screen, colorApple, [x_apple,y_apple],15)
        score = score + 1
        msg = font_style.render(f"Score: {score}", True, (100, 255,100),(100,40,200))

     



    #если нажали кнавишу
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y = y - 10
    if keys[pygame.K_s]:    
        y = y + 10
    if keys[pygame.K_a]: 
        x = x - 10
    if keys[pygame.K_d]:    
        x = x + 10


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

    pygame.display.flip()
pygame.quit()
