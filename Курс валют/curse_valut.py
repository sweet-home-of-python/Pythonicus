from pycbrf.toolbox import ExchangeRates
import os

data = '2019-05-08'

os.system('cls')
print('Что смотрим? USD или EUR?')
cons = input('Введи сюда: ')
os.system('cls')
if cons == '':
    print('Путое значение! Выбрана валюта по умолчанию')
    type = 'USD'
elif cons in ('USD','usd','dollar','доллар'):
    type = 'USD'
elif cons in ('EUR','eur','euro','евро'):
    type = 'EUR'
else:
    print('Ошибка! Выбрана валюта по умолчанию')
    type = 'USD'


rates = ExchangeRates(data)
name = rates[type].name
value = rates[type].value

print('''Курс валюты! v0.1
Название: {} 
Дата: {} 
Значение: {} руб.'''.format(name,data,value))