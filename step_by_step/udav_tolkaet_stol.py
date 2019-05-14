import pygame
import time 
from pomoshnik_udavu import *
DinamicObject()
while Play:
    sc.fill(WHITE)
    pygame.draw.circle(sc, some, (x, y), r)
    for obj_tag in GameObject.objects:
        GameObject.objects[obj_tag].draw(sc)
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

