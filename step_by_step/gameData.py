from pygame import draw
from random import randint

class GameObject:
    objects = {}
 


class StaticObject(GameObject):
      
    def __init__(self,desc = 'static object'):
  
        self.class_name = 'staticObject' + str(len(self.objects))
        self.class_tag = 'staticObject'
        self.desc = desc
                          
        self.pos = (0,0,0,0)
        self.type = 'rect'
        #self.params = [color,opacity]
        

        self.types = ('rect',
                      'circle')

        self.random_rect()

        GameObject.objects[self.class_name] = self
       

    def random_rect(self):
        self.type = 'rect'
        self.pos = (randint(0,1000),randint(0,600), randint(0,500), randint(0,500)) 

    def draw(self,screen):
        if self.type == 'rect':
            draw.rect(screen, colors['black'], self.pos)


def processingCollision(coords):
    x,y = coords
    for objkey in GameObject.objects:
        x1,y1,x2,y2 = GameObject.objects[objkey].pos
        if GameObject.objects[objkey].class_tag == 'staticObject':
             if (x in range(x1-50,x1+x2+50) 
                 and y in range(y1-30,y1+y2+30) 
                 or x in range(x1-30,x1+x2+30) 
                 and y in range(y1-50,y1+y2+50)) : #обработка столкновения
                 return True
             #else: return False

colors = {'black': (0,0,0),
          'white':(255,255,255),
          'red':(255,0,0),
          'green':(0,255,0),
          'blue':(0,0,255)
         }
            

