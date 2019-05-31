
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
s=0
y = 300
Play = True
sc.fill(white)
roll = False
direction = 1
speed =3 # задаешь удаву ускорение!
size = 10  # задаешь размеры ползучей сучары
luck =200






# задаешь как далеко он сможет проползти в одном направлении, если повезет конечно
color = (0,0,0)
dep_x = 0
dep_y = 0
iz = 0
sp_xy =[]
a = 0
sp_yx = []
w = 0
q = 0 
sp_main = []
 

def set_direction(x,y,s):
    
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
            s = 0
    return x,y,s

def choise_direct():
    pass

   
while Play:
    sp_yx=[x,y]
    if sp_yx in sp_main:
            
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
        
        step2 =  y + random.randint(0,luck)
        step1 = x + random.randint(0,luck)
        step3 = x - random.randint(0,luck)
        step4 = y - random.randint(0,luck)
        a = 1
    pygame.draw.rect(sc, color, (x,y,size,size))
    pygame.display.update()
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
        Play = False
       elif i.type == pygame.KEYDOWN:
        if i.key == pygame.K_LEFT:
            sc.fill(white)
            sp_xy = []
            sp_main=[]

    sp_xy = [x,y]
    sp_main.append(sp_xy)
    
    
    if a ==1:
        direction = random.choice([1,2,3,4])
        s = 1
        a=0
    if x > 1200 - size*2:
        direction = random.choice([2,3,4])
        s = 1
    if y > 600 - size*2:
        direction = random.choice([1,4,3])
        s = 1
    if x < + size * 2:
        direction = random.choice([1,2,4])
        s = 1
    if y < +size*2:
        direction = random.choice([1,2,3])
        s = 1

    

    x,y,s = set_direction(x,y,s)
     
        
  
    clock.tick(FPS)
