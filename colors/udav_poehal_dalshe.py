import pygame
 
pygame.init()

o = 0
sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
while o != 1 :
    x1 = 0 
    x2 = 0
    x3 = 0 
    a = 1
    b = 1
    c = 1
    speed = 1
    while 1:
        sc.fill((x1,x2,x3))
        if a ==1:
            if x3<254:
                x3+=speed
            if x3>=254:
                a=0
        if a ==0:
            if x3>0:
                x3-=speed
            if x3<=0:
                a=1
        if x3>=254 or x3 <= 0 or x3 ==120 or x3 ==60 or x3 ==180 or x3 ==30 :
            if b ==1 :
                x2+=speed
                if x2>=254:
                    b=0
            if b ==0 :
                x2-=speed
                if x2<=0:
                    b=1   
        if x2>=254 or x2<=0 or x2==120 or x2 ==60 or x2 ==180 or x2 ==30 :
            if c ==1 :
                x1+=speed
                if x1>=254:
                    c=0
            if c ==0 :
                x1-=speed
                if x1==0:
                    c=1 
        pygame.time.delay(1)
        pygame.display.update()
        if x1 ==255:
            break
    o = o+1
