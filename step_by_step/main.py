import pygame
import time 
from gameData import *


pygame.init()
Color = Color()
Person = Person()
Collision = Collision()



sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

#prestep_x,prestep_y = Person.prestep

Play = True 
motion = 'STOP'
while Play:
    sc.fill(Color.colors['white'])
    pygame.draw.circle(sc, Color.colors['black'], (Person.pos), Person.rad)
    for obj_tag in GameObject.objects:
        GameObject.objects[obj_tag].draw(sc)
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Play = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            Play = False
            pygame.quit()
        if keys[pygame.K_LEFT]:
            motion = 'LEFT'
        if keys[pygame.K_RIGHT]:
            motion = 'RIGHT'
        if keys[pygame.K_UP]:
            motion = 'UP'
        if keys[pygame.K_DOWN]:
            motion = 'DOWN'
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            motion = 'D_R'
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            motion = 'D_L'
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            motion = 'U_R'
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            motion = 'U_L'
        if keys[pygame.K_y]:
            StaticObject()
        if keys[pygame.K_r]:
            if len(GameObject.objects) > 0:
                del GameObject.objects['staticObject' + str(len(GameObject.objects)-1)]
        if keys[pygame.K_r] and keys[pygame.K_e]:
             GameObject.objects = {}
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = 'STOP'
    if Collision.processingCollision((x,y)):
        x=prestep_x
        y=prestep_y
    if motion == 'LEFT':
        prestep_x = x
        x -= 5
    if motion == 'RIGHT':
        prestep_x = x
        x += 5
    if motion == 'UP':
       prestep_y = y
       y -= 5
    if motion == 'DOWN':
        prestep_y = y
        y += 5
    if motion == 'D_R':
        prestep_x = x
        prestep_y = y
        y += 5
        x += 5
    if motion == 'D_L':
        prestep_x = x
        prestep_y = y
        y += 5
        x -= 5
    if motion == 'U_R':
        prestep_x = x
        prestep_y = y
        y -= 5
        x += 5
    if motion == 'U_L':
        prestep_x = x
        prestep_y = y
        y -= 5
        x -= 5
    clock.tick(Settings.fps)
