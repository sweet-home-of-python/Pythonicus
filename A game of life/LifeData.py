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
        self.health = 10
        self.starve = 10
        self.alive = True

        # Местоположение
        self.position = 100,200


        Objects.get_object(self)


    def random_gender(self):
        genders = ['male','female']
        return rand.choice(genders)

    def movenment(self):
        move_patterns = [0,1,2,3,4,5,6,7,8]
        move = rand.choice(move_patterns)
        x,y = self.position

        if move == 1: x-=10
        if move == 2: x-=10; y+=10
        if move == 3: y+=10
        if move == 4: x+=10; y+=10
        if move == 5: x+=10
        if move == 6: x+=10; y-=10
        if move == 7: y-=10
        if move == 8: x-=10; y-=10

        self.poposition = x,y

    def sensor(self):
        pass

    def life_control(self):
        pass



class Food:
    def __init__(self):
        
        self.position = 1,1



def pos_to_draw(position):
        '''Преобразует центральные координаты в координаты для квадрата'''
        size = 10
        x,y = position
        return  x - size, y - size, size * 2, size * 2