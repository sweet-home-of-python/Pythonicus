import pygame
import time 
from gameData import *
FPS = 60
W = 1200  
H = 700  
WHITE = (255, 255, 255)
black = (0, 0, 0)
some = (100, 50, 200)
D_R = "dr"
D_L ="dl"
U_R ="ur"
U_L ="ul"
STOP = "stop" 
RIGHT = "to the right"
LEFT = "to the left"
UP = "up"
DOWN = "down"
new = "ss"
prestep_x = W // 2
prestep_y = H // 2
x1w = 200
y1w = 200
x2w = 300
y2w = 350
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
x = W // 2
y = H // 2
r = 50
Play = True 
motion = STOP
ob1 = StaticObject('one')
ob1.random_rect()
x1w, y1w, x2w, y2w = ob1.pos
while Play:
    sc.fill(WHITE)
    pygame.draw.circle(sc, some, (x, y), r)
    ob1.draw(sc)
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
        if keys[pygame.K_y]:
            ob1.random_rect()
            ob1.draw(sc)
            x1w, y1w, x2w, y2w = ob1.pos
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = STOP
    if x in range(x1w-50,x1w+x2w+50) and y in range(y1w-30,y1w+y2w+30) or x in range(x1w-30,x1w+x2w+30) and y in range(y1w-50,y1w+y2w+50) : #обработка столкновения
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

