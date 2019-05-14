import pygame
from pygame import draw
from random import randint
FPS = 60
W = 1200  # ширина экрана
H = 700  # высота экрана
WHITE = (255, 255, 255)
black = (0, 0, 0)
some = (100, 50, 200)
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
class DinamicObject(GameObject):
      
    def __init__(self,desc = 'dinamic object'):
  
        self.class_name = 'dinamicObject' + str(len(self.objects))
        self.class_tag = 'dinamicObject'
        self.desc = desc
        self.pos = (0,0,0)
        self.type = 'rect'
        self.types = ('rect')

        self.random_rect()

        GameObject.objects[self.class_name] = self
    def random_rect(self):
        self.type = 'rect'
        self.pos = (700,300, 100, 100) 

    def draw(self,screen):
        if self.type == 'rect':
            draw.rect(screen, black, self.pos)

            
