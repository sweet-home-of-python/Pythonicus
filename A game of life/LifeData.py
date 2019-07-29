import random as rand
from pygame import draw

colors = {'black': (0,0,0), # пока не скопировал сюда из основного кода не работа draw
           'white':(255,255,255),
           'red':(255,0,0),
           'green':(0,255,0),
           'blue':(0,0,255)}

    
class Objects:
    objects = {}

    statistic = {'personObject':0,
                 'staticObject':0,
                 'dynamicObject':0
                 }

    def get_object(obj):
        Objects.objects[obj.class_name] = obj
        Objects.statistic[obj.class_tag] = Objects.statistic[obj.class_tag] + 1
    
    

class Person():
    def __init__(self, name):
        self.class_name = 'Person' + str(Objects.statistic['personObject'])
        self.class_tag = 'personObject'
        self.name = name

        # Особенности
        self.gender = self.random_gender()
        
        # параметры организма
        self.health = 100
        self.starve = 10
        self.alive = True

        # Местоположение
        self.position = 500,300
        self.step = 20


        Objects.get_object(self)
    

    def random_gender(self):
        genders = ['male','female']
        return rand.choice(genders)

    def movenment(self):
        move_direction = [0,1,2,3,4,5,6,7,8] # Направления дввижения. 0 - лево
        move = rand.choice(move_direction)
        x,y = self.position

        if move == 1: x-=10
        if move == 2: x-=10; y+=self.step
        if move == 3: y+=10
        if move == 4: x+=10; y+=self.step
        if move == 5: x+=10
        if move == 6: x+=10; y-=self.step
        if move == 7: y-=10
        if move == 8: x-=10; y-=self.step

        self.position = x,y

    def sensor(self):
        pass
        
    def draw(self,screen):
        '''отрисовка пиздюка'''
        draw.rect(screen,colors['black'],pos_to_draw(self.position)) # наверно надо будет тоже перенести в другой класс , чтобы не засорять класс перса 

    def life_control(self):
        print('poseluy mou zalupu')
        print('incest with young boys')

    def face_to_face(person1,person2):
        '''Обработка встречи, если одинаковый пол то махач, если разный то чпоканье'''
        if person1.gender == person2.gender:
            if person1.health > person2.health:
                del person2
            if person1.health < person2.health:
                del person1
        else:
           person = Person(person1.name + person2.name)
         # Я не знаю как правильно это написать, создание нового перса, и еще не уверен что удаление персов тоже сработает

class Food:
    def __init__(self):
        
        self.position = 1,1

class Spawner:
    '''Спавнит объекты'''
    pass



def pos_to_draw(position):
        '''Преобразует центральные координаты в координаты для квадрата'''
        size = 10
        x,y = position
        return  x - size, y - size, size * 2, size * 2