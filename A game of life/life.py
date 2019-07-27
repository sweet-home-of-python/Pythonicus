
import pygame
import time 
from LifeData import *


# Параметры окна
FPS = 60
Resolution = 1200,600  # размер экрана


pygame.init()
sc = pygame.display.set_mode(Resolution)
clock = pygame.time.Clock()


colors = {'black': (0,0,0),
           'white':(255,255,255),
           'red':(255,0,0),
           'green':(0,255,0),
           'blue':(0,0,255)}


pers = Person()
pers2 = Person()
pers3 = Person()
pers4 = Person()
pers5 = Person()
pers6 = Person()
sc.fill(colors['white']) # Заливка

Play = True # Запуск
a = 0 
while Play:
    sc.fill(colors['white']) # Заливка
    pers.movenment()
    pers2.movenment()
    pers3.movenment()
    pers4.movenment()
    pers5.movenment()
    pers6.movenment()
    pygame.draw.rect(sc,colors['black'],pos_to_draw(pers.position))
    pygame.draw.rect(sc,colors['black'],pos_to_draw(pers2.position))
    pygame.draw.rect(sc,colors['black'],pos_to_draw(pers3.position))
    pygame.draw.rect(sc,colors['black'],pos_to_draw(pers4.position))
    pygame.draw.rect(sc,colors['black'],pos_to_draw(pers5.position))
    pygame.draw.rect(sc,colors['black'],pos_to_draw(pers6.position))
    pygame.display.update()
    time.sleep(0.2)
   



    clock.tick(FPS)



