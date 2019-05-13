from pygame import draw
from random import randint
class staticObjects(object):
    def __init__(self,name):
        self.name = ''
        self.pos = (0,0,0,0)
        self.type = 'rect'
        #self.params = [color,opacity]
        self.colors = {'black': (0,0,0),
                       'white':(255,255,255),
                       'red':(255,0,0),
                       'green':(0,255,0),
                       'blue':(0,0,255)
                       }
        self.types = ('rect',
                      'circle'
                     )


    def random_rect(self):
        self.type = 'rect'
        self.pos = (randint(0,1000),randint(0,600), randint(0,500), randint(0,500)) 

    def drow(self,screen):
        if self.type == 'rect':
            draw.rect(screen, self.colors['black'], self.pos)