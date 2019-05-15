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
    colors = {'black': (0,0,0),
              'white':(255,255,255),
              'red':(255,0,0),
              'green':(0,255,0),
              'blue':(0,0,255)}
    def __init__(self):
        pass

    def random_color():
        color = (randint(0,255),randint(0,255),randint(0,255))
        return color


class GameObject:
    objects = {}
    
 
class Person:
   
    pos = 0,0
    size = 10
    speed = 2

    def __init__(self,size=10):
        self.class_name = 'Person' + str(len(GameObject.objects))
        self.class_tag = 'PersonObject'
        self.desc = ''
        self.pos = 10,10
        self.size = size
        self.coord = self.set_coord()
        self.prestep = self.pos

        GameObject.objects[self.class_name] = self
   
    def set_coord(self):
        x1,y1 = self.pos
        ret = x1-self.size, y1-self.size, self.size*2, self.size*2
        return ret

    def random_pos(self):
        self.pos = (randint(0,1000),randint(0,500))

    def draw(self,screen):
        draw.rect(screen, Color.random_color(), self.set_coord())

class StaticObject:
    def __init__(self,desc = 'static object'):
        # Инициализация
        self.class_name = 'staticObject' + str(len(GameObject.objects))
        self.class_tag = 'staticObject'
        self.desc = desc
                          
        self.pos = (0,0,0,0)

        self.mass = -1

        self.random_rect()
        
        GameObject.objects[self.class_name] = self
       

    def random_rect(self):
        self.pos = (randint(0,1000),randint(0,600), randint(0,500), randint(0,500)) 

    def draw(self,screen):
        draw.rect(screen, Color.colors['black'], self.pos)

class Settings:
    '''Настройки игры. Сюда входят параметры экрана и управления'''
    fps = 60
    def __init__(self):
        #fullscreen window
        self.mode = 'fullscreen'

    def init_screen(self):
        W = 1200  # ширина экрана
        H = 700  # высота экрана
        if self.mode == 'fullscreen':
            return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


class Collision:
    def processingCollision(coords):
        x,y = coords
        for objkey in GameObject.objects:
            if GameObject.objects[objkey].class_tag == 'staticObject':
                x1,y1,x2,y2 = GameObject.objects[objkey].pos
                if (x in range(x1-Person.size*2,x1+x2+Person.size*2) 
                    and y in range(y1-Person.size*2,y1+y2+Person.size*2) 
                    or x in range(x1-Person.size*2,x1+x2+Person.size*2) 
                    and y in range(y1-Person.size*2,y1+y2+Person.size*2)) : #обработка столкновения
                    print(objkey)
                    return True
                 #else: return False


