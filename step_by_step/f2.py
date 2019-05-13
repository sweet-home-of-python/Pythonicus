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
go = 1
prestep_x = W // 2
prestep_y = H // 2
x1w = 200
y1w = 200
x2w = 300
y2w = 350
gw1 = x2w-x1w
gw2 = y2w-y1w
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
# координаты и радиус круга
x = W // 2
y = H // 2
r = 50
Play = True 
motion = STOP
def _is_wall(x,y):
    pass
    
ob1 = staticObjects('one')
#ob2 = staticObjects('two')
ob1.random_rect()



def polet(vec,x):
    if vec ==6:
        while i.key == pygame.K_d:
            sc.fill(WHITE)
            x+=1
            pygame.draw.circle(sc, some, (x, y), r)
            pygame.display.update()
    return x 
x1w, y1w, x2w, y2w = ob1.pos
while Play:
    sc.fill(WHITE)
    pygame.draw.circle(sc, some, (x, y), r)
        
    ob1.drow(sc)
    
    pygame.display.update()
    
    for i in pygame.event.get():
        
        if i.type == pygame.QUIT:
            Play = False
        elif i.type == pygame.KEYDOWN:
            
            if i.key == pygame.K_LEFT:
                motion = LEFT
            if i.key == pygame.K_RIGHT:
                motion = RIGHT
            if i.key == pygame.K_UP:
                motion = UP
            if i.key == pygame.K_DOWN:
                motion = DOWN
            
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = STOP
        
    if x in range(x1w-50,x1w+x2w+50) and y in range(y1w-30,y1w+y2w+30) or x in range(x1w-30,x1w+x2w+30) and y in range(y1w-50,y1w+y2w+50) : #обработка столкновения
        x=prestep_x
        y=prestep_y
    if motion == LEFT :
        prestep_x = x
        x -= 3
    if motion == RIGHT :
        prestep_x = x
        x += 3
    if motion == UP :
       prestep_y = y
       y -= 3
    if motion == DOWN :
        prestep_y = y
        y += 3
    clock.tick(FPS)
