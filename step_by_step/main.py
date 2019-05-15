import pygame
import time 
from gameData import *


pygame.init()

Person1 = Person(30)
Person1.random_pos()



sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()


Play = True 

while Play:
    sc.fill(Color.colors['white'])
    
    #Person1.draw(sc)

    #Отрисовка всех объектов
    for obj_tag in GameObject.objects:
        GameObject.objects[obj_tag].draw(sc)


    pygame.display.update()

    x,y = Person1.pos
    prestep_x,prestep_y = Person1.prestep


    keys = pygame.key.get_pressed()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Play = False

            #Обработка отжатий
        if keys[pygame.K_ESCAPE]:
            Play = False
            pygame.quit()
        if keys[pygame.K_q]:
            Person1.speed +=1
            print(Person1.speed)
        if keys[pygame.K_a]:
            Person1.speed -=1
            print(Person1.speed)
        if keys[pygame.K_y]:
            StaticObject()
            print('\n',GameObject.objects)
        if keys[pygame.K_r]:
            if len(GameObject.objects) > 0:
                del GameObject.objects['staticObject' + str(len(GameObject.objects) - 1)]
        if keys[pygame.K_r] and keys[pygame.K_e]:
                GameObject.objects = {}
           
            
        #Обработка нажатий
    
    if keys[pygame.K_LEFT]:
        prestep_x = x
        x -= Person1.speed
    if keys[pygame.K_RIGHT]:
        prestep_x = x
        x += Person1.speed
    if keys[pygame.K_UP]:
        prestep_y = y
        y -= Person1.speed
    if keys[pygame.K_DOWN]:
        prestep_y = y
        y += Person1.speed

   
        
    # Коллизия
    Person1.prestep = prestep_x,prestep_y
    if Collision.processingCollision((x,y)):
        x,y = Person1.prestep

    Person1.pos = x,y
    clock.tick(Settings.fps)
