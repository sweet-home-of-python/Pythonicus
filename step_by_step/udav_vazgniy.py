import pygame
import time 
from gameData import *
FPS = 60
W = 1200  # ширина экрана
H = 700  # высота экрана
WHITE = (255, 255, 255)
black = (0, 0, 0)
some = (100, 50, 200)
STOP = "stop" 
RIGHT = "to the right"
LEFT = "to the left"
UP = "up"
DOWN = "down"
D_R = "dr"
D_L ="dl"
U_R ="ur"
U_L ="ul"
prestep_x = W // 2
prestep_y = H // 2
pygame.init()
sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
x = W // 2
y = H // 2
r = 50
Play = True 
motion = STOP
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
        if keys[pygame.K_ESCAPE]:
            Play = False
            pygame.quit()
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
        if keys[pygame.K_y]:
            StaticObject()
        if keys[pygame.K_r]:
            if len(GameObject.objects) > 0:
                del GameObject.objects['staticObject' + str(len(GameObject.objects)-1)]
        if keys[pygame.K_r] and keys[pygame.K_e]:
             GameObject.objects = {}
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = STOP
    if processingCollision((x,y)):
        x=prestep_x
        y=prestep_y
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
