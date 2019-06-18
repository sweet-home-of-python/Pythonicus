
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
s,iz,a,w,q=0,0,0,0,0
y = 300
Play = True
sc.fill(white)
roll = False
direction = 1
speed =3 # задаешь удаву ускорение!
size = 30  # задаешь размеры ползучей сучары
luck =200
# задаешь как далеко он сможет проползти в одном направлении, если повезет конечно
sp_y,sp_xy,sp_x,sp_yx,sp_main,sp_main2 =[],[],[],[],[],[]
spiss = [1,2,3,4]

while Play:
    
    rnd = random.randint(0,luck)  
    sp_xy=[x,y]
    sp_yx=[x+size,y+size]
 
    if sp_xy in sp_main:
        if direction == 1:
            x -=speed
            direction = random.choice([2,3,4])
           
        elif direction ==2:
            y -=speed
            direction = random.choice([1,4,3])
            
        elif direction == 3:
            x +=speed
            direction = random.choice([1,2,4])
            
        elif direction == 4:
            y +=speed
            direction = random.choice([1,2,3])
    if s == 0 :
        step1,step2 =  x+ rnd,y+ rnd
        step3,step4 = x- rnd,y- rnd
        a = 1
    pygame.draw.rect(sc, black, (x,y,size,size))
    pygame.display.update()
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
        Play = False
       elif i.type == pygame.KEYDOWN:
        if i.key == pygame.K_LEFT:
            pass
    
    sp_x = [x,y]
    sp_y = [x+size,y+size]
    sp_main.append(sp_x)
    sp_main2.append(sp_y)
    if a ==1:
        direction = random.choice([1,2,3,4])
        s = 1
        a=0
    if x > 1200- size*2:
        direction = random.choice([2,3,4])
        s = 1
    if y > 600 - size*2:
        direction = random.choice([1,4,3])
        s = 1
    if x < +size*2:
        direction = random.choice([1,2,4])
        s = 1
    if y < +size*2:
        direction = random.choice([1,2,3])
        s = 1
    if direction == 1 :
        if x < step1:
            x+=speed
        else:
            s =0
    if direction == 2 :
        if y < step2:
            y+=speed
        else:
            s =0
    if direction == 3 :
        if x > step3:
            x-=speed 
        else:
            s =0 
    if direction == 4 :
        if y > step4:
            y-=speed
        else:
            s =0
    clock.tick(FPS)
