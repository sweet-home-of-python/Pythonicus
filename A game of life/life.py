
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
           'blue':(0,0,255)} # цвета


pers = Person("jake")# пиздюки
pers2 = Person("fin")
pers3 = Person("jake")
pers4 = Person("fin")
pers5 = Person("jake")
pers6 = Person("fin")
pers7 = Person("jake")
pers8 = Person("fin")
pers9 = Person("jake")
pers10 = Person("fin")
sc.fill(colors['white']) # Заливка

Play = True # Запуск
a = 0 
while Play:
    sc.fill(colors['white'])# Заливка
    for obj_tag in Objects.objects: # обработка всех объектов
        Objects.objects[obj_tag].movenment()
        Objects.objects[obj_tag].draw(sc)
    pygame.display.update()
    time.sleep(0.1)
    clock.tick(FPS)



