from pygame import draw
from random import randint
class staticObjects(object):
    def __init__(self,name,pos,*params):
        self.name = ''
        self.pos = (0,0,0,0)
        self.params = [color,opacity]
        self.colors = {'black': (0,0,0),
                       'white':(255,255,255),
                       'red':(255,0,0),
                       'green':(0,255,0),
                       'blue':(0,0,255)
                       }


    def random_rect(self,screen):
        self.pos = (randint(0,1000),randint(0,1000), randint(0,100), randint(0,100))
        draw.rect(screen, self.colors['black'], self.pos)
        return self.pos