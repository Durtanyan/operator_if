# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 10:49:46 2020

@author: lukin
"""

import random
import time
#Из этой строки будем рандомно имититовать названия городов
c = "QWERTYUIOPASDFGHJKLZXCVBNM"
cities= []

#Рандомно создаем имитацию списка городов из 20000 наименований
b = 0 #количество итераций
while b <= 20000:
	e = ""
	for i in range(random.randint(3, 5)):
		j = 0
		while j <= i:
			e += c[random.randint(0, len(c) - 1)]
			j += 1
	cities.append(e)
	b += 1

#С помощью сета удаляем дубли, знаю, что можно было сразу
#имитировать не в список а в сет, но мне так приспичило
cities = set(cities)
#Листуем данные без дублей
cities = list(cities)

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = []

#Подготавливаем финальный список tourists = [] словарей, я ограничился 
#тремя юзерами из списка словарей users.	
for i in cities:
    #очищаем словарь, чтобы на каждой из 20000 итераций
    #записывать в него новые данные и пополнять ими список tourists = []
	dict_users = {}
    #рандомно выбираем юзера из списка users
	l = random.randint(0, 2)
    #формируем данные словаря для списка tourists = []
	dict_users['user'] = users[l]
	dict_users['city'] = i
    #добавляем сформированные словари в список tourists = []
	tourists.append(dict_users)

print("Данные заполнены!")
#город для теста. Один из 20000
print(f"Город для теста: {cities[random.randint(0, len(cities) - 1)]}")
print("----------")

city = input('Введите город: ')

print("------------")

"""
ПАРСИНГ ЧЕРЕЗ VALUE()
"""
print('____________________')
print('РЕШЕНИЕ ЗАДАЧИ РАСПАРСИВАНИЕМ СЛОВАРЕЙ ИЗ СПИСКА ЧЕРЕЗ VALUE()')

a = float(time.time())
#создаем финальный словарь индексации
c = dict()
try:
	city[0]
except IndexError:
	print("Вы не ввели город.")
else:
	if city in cities:
		for v in tourists:
			if city in v.values():
				print(f"Турист {v['user']['name']} возраст {v['user']['age']}. Посетил город  {city}.")
	else:
		print("Такого города в списке нет.")
b = float(time.time())
print(f"Парсинг через value(): {(b - a):.20}")
#добавляем данные в финальный словарь который будем индексировать по возрастанию
c["value"] = (b - a)

#------------------

"""
ПАРСИНГ ЧЕРЕЗ ENUMERATE()
"""
print('____________________')
print('РЕШЕНИЕ ЗАДАЧИ РАСПАРСИВАНИЕМ СЛОВАРЕЙ ИЗ СПИСКА ЧЕРЕЗ ENUMERATE()')
a = float(time.time())
try:
	city[0]
except IndexError:
	print("Вы не ввели город.")
else:
	if city in cities:
		for k, v in enumerate(tourists):
			if city in v['city']:
				print(f"Турист {v['user']['name']} возраст {v['user']['age']}. Посетил город  {city}.")
	else:
		print("Такого города в списке нет.")
b = float(time.time())
print(f"Парсинг через enumerate(): {(b - a):.20}")
#добавляем данные в финальный словарь который будем индексировать по возрастанию
c["enumerate"] = (b - a)

#---------------------

"""
ПАРСИНГ ЧЕРЕЗ ITER()
"""
print('____________________')
print('РЕШЕНИЕ ЗАДАЧИ РАСПАРСИВАНИЕМ СЛОВАРЕЙ ИЗ СПИСКА ЧЕРЕЗ ITER()')

a = float(time.time())
try:
	city[0]
except IndexError:
	print("Вы не ввели город.")
else:
	if city in cities:
		for v in iter(tourists):
			if city in v['city']:
				print(f"Турист {v['user']['name']} возраст {v['user']['age']}. Посетил город  {city}.")
	else:
		print("Такого города в списке нет.")
b = float(time.time())
print(f"Парсинг через iter(): {(b - a):.20}")
#добавляем данные в финальный словарь который будем индексировать по возрастанию
c["iter"] = (b - a)

#------------

"""
РЕШЕНИЕ ЗАДАЧИ ПРЯМЫМ РАСПАРСИВАНИЕМ СЛОВАРЕЙ ИЗ СПИСКА
"""
print('____________________')
print('РЕШЕНИЕ ЗАДАЧИ ПРЯМЫМ РАСПАРСИВАНИЕМ СЛОВАРЕЙ ИЗ СПИСКА')

a = float(time.time())
try:
	city[0]
except IndexError:
	print("Вы не ввели город.")
else:
    if city in cities:
        for i in tourists:
            for key in i:
                if i[key] == city:
                    for j in i:
                        if j == 'user':
                            print(f"Турист {i[j]['name']} возраст {i[j]['age']}. Посетил город {city}.")
    else:
        print("Такого города в списке нет.")
        
b = float(time.time())
print(f"Прямой парсинг словарей из списков: {(b - a):.20}")
#добавляем данные в финальный словарь который будем индексировать по возрастанию
c["Прямой"] = (b - a)

#Финальный словарь индексации
print("----------")
print('ПОЛУЧИВШИЙСЯ СЛОВАРЬ:')
print(c)
print("----------")
#сортируем данные словаря
print("СРАВНЕНИЕ СКОРОСТИ ПО ВОЗРАСТАНИЮ.")
list_c = list(c.items())
list_c.sort(key=lambda i: i[1])
for i in list_c:
	print(i[0], ':', i[1])	
