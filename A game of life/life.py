
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


sc.fill(colors['white']) # Заливка

Play = True # Запуск

while Play:
    sc.fill(colors['white']) # Заливка
    pers.movenment()

    pygame.draw.rect(sc,colors['black'],pos_to_draw(pers.position))
      
    pygame.display.update()




