import pygame
import time 
from pomoshnik_udavu import *
StaticObject()
while Play:
    sc.fill(WHITE)
    pygame.draw.circle(sc, some, (x, y), r)
    pygame.draw.rect(sc, black, (x1,y1,x2,y2))
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Play = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            motion = LEFT
        if keys[pygame.K_RIGHT]:
            motion = RIGHT
        if keys[pygame.K_UP]:
            motion = UP
        if keys[pygame.K_DOWN]:
            motion = DOWN
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            motion = rad_p
        if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            motion = rad_m
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            motion = D_R
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            motion = D_L
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            motion = U_R
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            motion = U_L
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = STOP
    
    if (x in range(x1-r,x1+x2+r +1) 
                 and y in range(y1-r+20,y1+y2+r-20) 
                 or x in range(x1-r+20,x1+x2+r-20) 
                 and y in range(y1-r,y1+y2+r+1)):
        if r < 50:
            a =1
        
        if motion == LEFT :
           if y+r != y1 and y-r != y1+y2:
                if prestep_x > x:
                    x1-=int(r/50*5)
        if motion == RIGHT:
           if y+r != y1 and y-r != y1+y2:
             if prestep_x < x:
                x1+=int(r/50*5)
        if motion == UP:
           if x+r != x1 and x-r != x1+x2:
               if prestep_y > y:
                 y1-=int(r/50*5)
        if motion == DOWN:
           if x+r != x1 and x-r != x1+x2:
               if prestep_y < y:
                y1+=int(r/50*5)
        if motion == D_R:
            if x<x1:
               if  prestep_y < y:
                   if y+r != y1 and y-r != y1+y2:
                     if prestep_x < x:
                        x1+=int(r/50*5)
            if x>x1:
               if  prestep_y < y:
                   if y+r != y1 and y-r != y1+y2:
                     if prestep_x < x:
                        y1+=int(r/50*5)
        if motion == D_L:
           if x>x1+x2:
               if  prestep_y < y:
                    if y+r != y1 and y-r != y1+y2:
                        if prestep_x > x:
                            x1-=int(r/50*5)
           if x<x1+x2:
               if  prestep_y < y:
                   if y+r != y1 and y-r != y1+y2:
                     if prestep_x > x:
                        y1+=int(r/50*5)
        if motion == U_R:
           if x<x1:
               if  prestep_y > y:
                   if y+r != y1 and y-r != y1+y2:
                     if prestep_x < x:
                        x1+=int(r/50*5)
           if x>x1:    
               if  prestep_x < x:
                   if x+r != x1 and x-r != x1+x2:
                       if prestep_y > y:
                            y1-=int(r/50*5)
        if motion == U_L:
           if x>x1+x2:
               if  prestep_y > y:
                   if y+r != y1 and y-r != y1+y2:
                        if prestep_x > x:
                            x1-=int(r/50*5)
           if x<x1+x2:    
               if  prestep_x > x:
                   if x+r != x1 and x-r != x1+x2:
                       if prestep_y > y:
                            y1-=int(r/50*5)
    if motion == LEFT :
        if a ==1:
            prestep_x = x
            x -= int(r/50*5)
        if r >= 50 and a ==0:
            prestep_x = x
            x -= int(5*50/r)
        if r < 50 and a ==0:
            prestep_x = x
            x -= int(5*50/r)
        a = 0
    if motion == RIGHT :
        if a ==1:
            prestep_x = x
            x += int(r/50*5)
        if r >= 50 and a ==0:
            prestep_x = x
            x += int(5*50/r)
        if r < 50 and a ==0:
            prestep_x = x
            x += int(5*50/r)
        a = 0
    if motion == UP :
        if a ==1:
            prestep_y = y
            y -= int(r/50*5)
        if r >= 50 and a ==0:
            prestep_y = y
            y -= int(5*50/r)
        if r < 50 and a ==0:
            prestep_y = y
            y -= int(5*50/r)
        a = 0
    if motion == DOWN :
        if a ==1:
            prestep_y = y
            y += int(r/50*5)
        if r >= 50 and a ==0:
            prestep_y = y
            y += int(5*50/r)
        if r < 50 and a ==0:
            prestep_y = y
            y += int(5*50/r)
        a = 0
    if motion == D_R :
        if a ==1:
            prestep_x = x
            prestep_y = y
            y += int(r/50*5)
            x += int(r/50*5)
        if r >= 50 and a ==0:
            prestep_x = x
            prestep_y = y
            y += int(5*50/r)
            x += int(5*50/r)
        if r < 50 and a ==0:
            prestep_x = x
            prestep_y = y
            y += int(5*50/r)
            x += int(5*50/r)
        a = 0
            
    if motion == D_L :
        if a ==1:
            prestep_x = x
            prestep_y = y
            y += int(r/50*5)
            x -= int(r/50*5)
        if r >= 50 and a ==0:
            prestep_x = x
            prestep_y = y
            y += int(5*50/r)
            x -= int(5*50/r)
        if r < 50 and a ==0:
            prestep_x = x
            prestep_y = y
            y += int(5*50/r)
            x -= int(5*50/r)
        a = 0
        
            
    if motion == U_R :
        if a ==1:
            prestep_x = x
            prestep_y = y
            y -= int(r/50*5)
            x += int(r/50*5)
        if r >= 50 and a ==0:
            prestep_x = x
            prestep_y = y
            y -= int(5*50/r)
            x += int(5*50/r)
        if r < 50 and a ==0:
            prestep_x = x
            prestep_y = y
            y -= int(5*50/r)
            x += int(5*50/r)
        a = 0
    if motion == U_L :
        if a ==1:
            prestep_x = x
            prestep_y = y
            y -= int(r/50*5)
            x -= int(r/50*5)
        if r >= 50 and a == 0:
            prestep_x = x
            prestep_y = y
            y -= int(5*50/r)
            x -= int(5*50/r)
        if r < 50 and a ==0:
            prestep_x = x
            prestep_y = y
            y -= int(5*50/r)
            x -= int(5*50/r)
        a = 0
    if motion == rad_p :
        r+=1
    if motion == rad_m :
        r-=1
    clock.tick(FPS)