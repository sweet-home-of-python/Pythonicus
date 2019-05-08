import pygame
 
pygame.init()
x1 = 0 
x2 = 0
x3 = 0 

sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

while True:
    sc.fill((x1,x2,x3))
    if x1<255:
        x1+=1
    if x1 == 255:
        if x2 < 255:
            x2+=1
    if x2 == 255:
        if x3 < 255:
            x3+=1   
    pygame.time.delay(10) 
    pygame.display.update()