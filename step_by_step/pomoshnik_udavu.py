import pygame
from pygame import draw
from random import randint
x1=700
x2=100
y1=300
y2=100
FPS = 60
W = 1200  # ширина экрана
H = 700  # высота экрана
a = 0
WHITE = (255, 255, 255)
black = (0, 0, 0)
some = (100, 50, 200)
rad_p = "radius+"
rad_m = "radius-"
STOP = "stop" 
RIGHT = "to the right"
LEFT = "to the left"
UP = "up"
DOWN = "down"
D_R = "dr"
D_L ="dl"
U_R ="ur"
U_L ="ul"
prestep_x = W // 2
prestep_y = H // 2
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
x = W // 2
y = H // 2
r = 50
Play = True 
motion = STOP
class GameObject:
    objects = {}
    key_objects = []
 


class StaticObject(GameObject):
      
    def __init__(self,desc = 'static object'):
  
        self.class_name = 'staticObject' + str(len(self.objects))
        self.class_tag = 'staticObject'
        self.desc = desc
                          
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
                      'circle')

        self.random_rect()

        GameObject.objects[self.class_name] = self
        GameObject.key_objects.append(self.class_name) 

    def random_rect(self):
        self.type = 'rect'
        self.pos = (x1,y1, x2, y2) 

    def draw(self,screen):
        if self.type == 'rect':
            draw.rect(screen, self.colors['black'], self.pos)

    
        
def processingCollision(coords):
    x,y = coords
    for objkey in GameObject.objects:
        x2,y2,x3,y3 = GameObject.objects[objkey].pos
        if GameObject.objects[objkey].class_tag == 'staticObject':
             
             if (x in range(x2-50,x2+x3+50) 
                 and y in range(y2-50,y2+y3+50) 
                 or x in range(x2-50,x2+x3+50) 
                 and y in range(y2-50,y2+y3+50)) : #обработка столкновения
                 return True
                
             #else: return False

    
    