import random as rand



    
class Objects:
    objects = {}

    statistic = {'personObject':0,
                 'staticObject':0,
                 'dynamicObject':0
                 }

    def get_object(obj):
        Objects.objects[obj.class_name] = obj
        Objects.statistic[obj.class_tag] = Objects.statistic[obj.class_tag] + 1



class Person:
    def __init__(self):
        self.class_name = 'Person' + str(Objects.statistic['personObject'])
        self.class_tag = 'personObject'


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

        if move == 1: 
            x-=10
        if move == 2: x-=10; y+=self.step
        if move == 3: y+=10
        if move == 4: x+=10; y+=self.step
        if move == 5: x+=10
        if move == 6: x+=10; y-=self.step
        if move == 7: y-=10
        if move == 8: x-=10; y-=self.step

        self.position = x,y

    def sensor(self):
        
        cell = 0
        x,y = self.position
        

    def life_control(self):
        print('poseluy mou zalupu')
        print('incest with young boys')

    def pidor():
        
        

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