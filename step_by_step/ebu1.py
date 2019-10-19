import pygame
import time 
from pomoshnik_udavu import *
x3,y3 = x2,y2
x4,y4 = x,y
while Play:
    sc.fill(WHITE)
    pygame.draw.rect(sc, black, (x,y,20,20))
    pygame.draw.rect(sc, black, (x2,y2,20,20))
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Play = False
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
             x2 -=10
        if keys[pygame.K_d]:
            x2+=10
        if keys[pygame.K_w]:
            y2-=10
        if keys[pygame.K_s]:
            y2+=10
        if keys[pygame.K_LEFT]:
            x -=10
        if keys[pygame.K_RIGHT]:
            x+=10
        
        if keys[pygame.K_UP]:
             y-=10
       
        if keys[pygame.K_DOWN]:
            y+=10
        #if keys[pygame.K_f]:
        #    x3,y3 = x2,y2
        #    xx1 = x3 + 200
        #    while x3!= xx1:
        #     pygame.draw.rect(sc, black, (x3,y3,5,5))
        #     pygame.display.update()
        #     x3+=1
        #    motion = STOP
        #if keys[pygame.K_p]:
        #    x4,y4 = x,y
        #    xx2 = x4 - 200
        #    while x4!= xx2:
        #     pygame.draw.rect(sc, black, (x4,y4,5,5))
        #     pygame.display.update()
        #     x4-=1
        #    motion = STOP
        
  
 
    
    
       
    clock.tick(FPS)
