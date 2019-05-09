import pygame
 
pygame.init()

o = 0
sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
while o != 3 :
    x1 = 0 
    x2 = 0
    x3 = 0 
    while 1:
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
        if x3 ==255:
            break
    o = o+1