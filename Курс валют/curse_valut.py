from pycbrf.toolbox import ExchangeRates
import os

data = '2018-05-08'

rates = ExchangeRates(data)
name = rates['USD'].name
value = rates['USD'].value
nam = 'dolar'
val = '123'

os.system('cls')
print('''Курс валюты! v0.1
Название: {} 
Дата: {} 
Значение: {}'''.format(name,data,value))