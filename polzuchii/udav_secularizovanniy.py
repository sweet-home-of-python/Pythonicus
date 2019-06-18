# ver 0.1
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



class Udav():
    def __init__(self, name):
        self.name = name
        
        #Параметры этой гадюки
        self.speed = 3 # задаешь удаву ускорение!
        self.size = 10  # задаешь размеры ползучей сучары

        self.direction = ''
        self.random_direct()
        self.position = 400,300

        self.allcoord = []

    def random_direct(self):
        directions = ['left','right','up','down']
        self.direction = random.choice(directions)
         
    def set_coord_to_draw(self):
        x,y = self.position
        return  x - self.size, y - self.size, self.size * 2, self.size * 2
    
    def movement(self):

        global Resolution

        prestep = self.position

        x,y = self.position
        if self.direction == 'left':
            x += round(self.size / 2)
        if self.direction == 'right':
            x -= round(self.size / 2)
        if self.direction == 'up':
            y += round(self.size / 2)
        if self.direction == 'down':
            y -= round(self.size / 2)
        self.position = x,y

        print(self.position)

        if self.position > Resolution or self.position < (0,0):
            self.position = prestep
        
        

    def collision(self):
        precoord = self.position
   
    def draw_rect(self,screen,color):
        
        pygame.draw.rect(screen,color,self.set_coord_to_draw())



#Создание шакалов капашащихся
sc.fill(colors['white']) #Замалафили экран ъУъ СУКА!
udav = Udav('udavsk')

Play = True # Разрешение на ползучесть

while Play:
    udav.movement()
    udav.draw_rect(sc,colors['black'])

    udav.random_direct()
    pygame.display.update()