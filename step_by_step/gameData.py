# GameData Версия 0.67
# 
#
#
#
#


from pygame import draw
from random import randint

class Color:
    '''Работает с RGB цветами'''
    def __init__(self):
        self.colors = {'black': (0,0,0),
                        'white':(255,255,255),
                        'red':(255,0,0),
                        'green':(0,255,0),
                        'blue':(0,0,255)
                      }
    def random_color():
        return randint(0,256),randint(0,256),randint(0,256)


class GameObject:
    objects = {}
 
class Person:
    def __init__(self):
        self.pos = (0,0)
        self.rad = 50
        #self.screen = screen
        self.prestep = self.pos
    
    def random_pos(self):
        self.pos = (randint(0,1000),randint(0,500))
        self.prestep = self.pos
    
    def draw(self):
        pygame.draw.circle(self.screen, Color.random_color(), (self.pos), self.rad)

class StaticObject:
    def __init__(self,desc = 'static object'):
        # Инициализация
        self.class_name = 'staticObject' + str(len(self.objects))
        self.class_tag = 'staticObject'
        self.desc = desc
                          
        self.pos = (0,0,0,0)

        self.random_rect()
        
        GameObject.objects[self.class_name] = self
       

    def random_rect(self):
        self.pos = (randint(0,1000),randint(0,600), randint(0,500), randint(0,500)) 

    def draw(self,screen):
        draw.rect(screen, Color.colors['black'], self.pos)

class Settings:
    '''Настройки игры. Сюда входят параметры экрана и управления'''
    def __init__(self):
        #fullscreen window
        self.mode = 'fullscreen'
        self.fps = 60

    def init_screen(self):
        W = 1200  # ширина экрана
        H = 700  # высота экрана
        if self.mode == 'fullscreen':
            return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


class Collision:
    def processingCollision(coords):
        x,y = coords
        for objkey in GameObject.objects:
            x1,y1,x2,y2 = GameObject.objects[objkey].pos
            if GameObject.objects[objkey].class_tag == 'staticObject':
                 if (x in range(x1-50,x1+x2+50) 
                     and y in range(y1-50,y1+y2+50) 
                     or x in range(x1-50,x1+x2+50) 
                     and y in range(y1-50,y1+y2+50)) : #обработка столкновения
                     return True
                 #else: return False

