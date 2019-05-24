import pygame
import time 
import random
FPS = 60
W = 1200  # ширина экрана
H = 600  # высота экрана
white = (255, 255, 255)
black = (0, 0, 0)
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
# координаты и радиус круга
x = 400
y = 300
Play = True
sc.fill(white)
roll = False
direction = 0
speed =5 # задаешь удаву ускорение
size = 200  # задаешь размеры ползучей сучары
luck =20    # задаешь как далеко он сможет проползти в одном направлении, если повезет конечно
color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
while Play:
    
    if roll == False or roll == True :
        
        step2 =  y + random.randint(0,luck)
        step1 = x + random.randint(0,luck)
        step3 = x - random.randint(0,luck)
        step4 = y - random.randint(0,luck)
    pygame.draw.rect(sc, color, (x,y,size,size))
    pygame.display.update()
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
        Play = False
       elif i.type == pygame.KEYDOWN:
        if i.key == pygame.K_LEFT:
            pass
    
    if x >= 1200-size :
        direction = 1
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if x <= 0:
        direction = 0
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if y >= 600-size:
        direction =1
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if y <=0:
        direction = 0
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if roll == False:
        if direction == 0 :
            if x < step1:
                x+=speed
            else:
                roll = True
                color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                
        elif direction == 1 :
            if x > step3:
                x-=speed
            else:
                roll = True
                color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
    if roll == True:
        if direction == 0:
            if y < step2:
                y+=speed
            else:
                roll = False
                color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
        elif direction == 1:
            if y > step4:
                y-=speed
            else:
                roll = False
                color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if roll == False:
            direction = random.randint(0,1)
   
    clock.tick(FPS)
