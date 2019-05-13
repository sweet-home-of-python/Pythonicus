import pygame
import time 
FPS = 60
W = 1200  # ширина экрана
H = 700  # высота экрана
WHITE = (255, 255, 255)
black = (0, 0, 0)
 
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
# координаты и радиус круга
x = W // 2
y = H // 2
r = 50
Play = True 
def polet(z,vec,x,y):
    if vec == 6:
        while x < z:
            pygame.time.delay(2)
            sc.fill(WHITE)
            x += 2
            pygame.draw.circle(sc, black, (x, y), r) 
            pygame.display.update()
            if vec != 6:
                break
                
    if vec == 4:
        while x > z:
            pygame.time.delay(2)
            sc.fill(WHITE)
            x -= 2
            pygame.draw.circle(sc, black, (x, y), r) 
            pygame.display.update()
        
    if vec == 8:
        while y > z:
            pygame.time.delay(2)
            sc.fill(WHITE)
            y -= 2
            pygame.draw.circle(sc, black, (x, y), r) 
            pygame.display.update()
                  
    if vec == 2:
        while y < z:
            pygame.time.delay(2)
            sc.fill(WHITE)
            y += 2
            pygame.draw.circle(sc, black, (x, y), r) 
            pygame.display.update()
    return x,y
     
while Play:
    sc.fill(WHITE)
 
    pygame.draw.circle(sc, black, (x, y), r)
 
    pygame.display.update()
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Play = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 3
            elif i.key == pygame.K_RIGHT:
                x += 3
            elif i.key == pygame.K_UP:
                y -= 3
            elif i.key == pygame.K_DOWN:
                y += 3
            elif i.key == pygame.K_d:
                x,y = polet(x + 200, 6,x, y)
            elif i.key == pygame.K_s:
                x,y = polet(y + 200, 2,x, y)
            elif i.key == pygame.K_a:
                x,y = polet(x - 200, 4,x, y)
            elif i.key == pygame.K_w:
                x,y = polet(y - 200, 8,x, y)        
    clock.tick(FPS)