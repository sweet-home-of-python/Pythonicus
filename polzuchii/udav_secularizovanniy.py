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
        self.speed = 3 # задаешь удаву ускорение! (нет)
        self.size = 10  # задаешь размеры ползучей сучары

        self.direction = ''
        self.random_direct()
        self.position = 400,300

        self.allcoord = []

    def random_direct(self):
        '''Возвращает случаюное направление'''
        directions = ['left','right','up','down']
        self.direction = random.choice(directions)
         
    def set_coord_to_draw(self):
        '''Преобразует центральные координаты в координаты для квадрата'''
        x,y = self.position
        return  x - self.size, y - self.size, self.size * 2, self.size * 2
    
    def movement(self):

        prestep = self.position

        x,y = self.position
        if self.direction == 'left':
            x += 2 * self.size
        if self.direction == 'right':
            x -= 2 * self.size
        if self.direction == 'up':
            y += 2 * self.size
        if self.direction == 'down':
            y -= 2 * self.size
           
        
        self.position = x,y
        
        if self.collision():
            self.position = prestep

        # Проверяем нет ли уже такой координаты, чтоб не повторяться
        if self.position not in self.allcoord:
            self.allcoord.append(self.position)
        
        
        #print(self.position)

        

    def collision(self):
        x,y = self.position
        global Resolution
        sx,sy = Resolution
        if self.position in self.allcoord:
            return True
        #if (x+self.size,y+self.size) in self.allcoord or (x-self.size,y-self.size) in self.allcoord:
           # return True
        elif x >= sx or x <= 0 or y >= sy or y <= 0:
            return True
        else: return False
   
    def draw_rect(self,screen,color):
        
        pygame.draw.rect(screen,color,self.set_coord_to_draw())



#Создание шакалов капашащихся
sc.fill(colors['white']) #Замалафили экран ъУъ СУКА!
udav = Udav('udavsk')

Play = True # Разрешение на ползучесть
i = 1
while Play:
    udav.movement()
    rand = random.randint(0,255)
    udav.draw_rect(sc,colors['black'])
    if i <= 0:
        udav.random_direct()
        i = random.randint(2,4)
    i -= 1

    

    pygame.display.update()