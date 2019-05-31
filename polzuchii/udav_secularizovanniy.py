
import pygame
import time 
import random


# Параметры наблюдательного, о кошка!
FPS = 60
Resolution = 1200,600  # размер экрана


colors = {'black': (0,0,0),
           'white':(255,255,255),
           'red':(255,0,0),
           'green':(0,255,0),
           'blue':(0,0,255)}


#Инициализация длиннохвостого ублюдка
pygame.init()
sc = pygame.display.set_mode(Resolution)
clock = pygame.time.Clock()



#Параметры этой гадюки
speed = 3 # задаешь удаву ускорение!
size = 10  # задаешь размеры ползучей сучары

x,y = 400,300


sc.fill(colors['white']) #Замалафили экран  ъУъ СУКА!


Play = True # Разрешение на ползучесть


# ФункциАНАЛ
def set_coord(x,y,size):
    return  x-size, y-size, size*2, size*2


def collision(x,y,size):
    pass