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
    if (x in range(x1-50,x1+x2+50) 
                 and y in range(y1-30,y1+y2+30) 
                 or x in range(x1-30,x1+x2+30) 
                 and y in range(y1-50,y1+y2+50)):
       if motion == LEFT :
           if y+50 != y1 and y-50 != y2:
                if prestep_x > x:
                    x1-=5
       if motion == RIGHT:
           if y+50 != y1 and y-50 != y2:
             if prestep_x < x:
                x1+=5
       if motion == UP:
           if x+50 != x1 and x-50 != x2:
               if prestep_y > y:
                 y1-=5
       if motion == DOWN:
           if x+50 != x1 and x-50 != x2:
            if prestep_y < y:
                y1+=5
               
           
            

    if motion == LEFT :
        prestep_x = x
        x -= 5
    if motion == RIGHT :
        prestep_x = x
        x += 5
    if motion == UP :
       prestep_y = y
       y -= 5
    if motion == DOWN :
        prestep_y = y
        y += 5
    if motion == D_R :
        prestep_x = x
        prestep_y = y
        y += 5
        x += 5
    if motion == D_L :
        prestep_x = x
        prestep_y = y
        y += 5
        x -= 5
    if motion == U_R :
        prestep_x = x
        prestep_y = y
        y -= 5
        x += 5
    if motion == U_L :
        prestep_x = x
        prestep_y = y
        y -= 5
        x -= 5
    clock.tick(FPS)

