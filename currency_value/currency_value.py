from pycbrf.toolbox import ExchangeRates
import os

import datetime

now = datetime.datetime.now()


currency = []
names = []


os.system('cls')
print('Выбор валюты:')


date = now.date() # Текущая дата

data = ExchangeRates(date) #

rates = data.rates

#Создает список из кодов и имен валют
for i in rates:
    currency.append(i[2])
    names.append(i[1])
n = 1
for i in currency:
    print('{}) ({}) {}'.format(n,i,names[n-1]))
    n+=1

num = int(input('Введите номер валюты: '))

if num < len(currency) and num > 0:
    type = currency[num-1]
else: type = 'USD'
    

name = data[type].name
value = data[type].value


os.system('cls')
print('''Информация:
Название: {} 
Дата: {} 
Значение: {} руб.'''.format(name,date,value))

print('\nКонвертер:')

val = int(input('Сколько у тебя валюты?: '))

print('Результат: {} руб.'.format(val * value))
input()

print('\ncreate by YarLikViD. Ver 1.0a')
