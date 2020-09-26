# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 10:49:46 2020

@author: lukin
"""

import random
import time
b = 0
c = "QWERTYUIOPASDFGHJKLZXCVBNM"
d = []
cities= []

for i in c:
	d.append(i)

while b <= 20000:
	e = ""
	for i in range(random.randint(3, 5)):
		j = 0
		while j <= i:
			e += c[random.randint(0, len(c) - 1)]
			j += 1
	cities.append(e)
	
	b += 1

cities = set(cities)
cities = list(cities)

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = []
	
for i in cities:
	dict_users = {}
	l = random.randint(0, 2)
	dict_users['user'] = users[l]
	dict_users['city'] = i
	tourists.append(dict_users)

print("Данные заполнены!")
print(f"Город для теста: {cities[random.randint(0, len(cities) - 1)]}")
print("----------")


city = input('Введите город: ')
print(city)
print(len(cities))
print("------------")

a = float(time.time())
c = dict()
try:
	city[0]
except:
	print("Вы не ввели город.")
else:
	if city in cities:
		for v in tourists:
			if city in v.values():
				print(f"Турист {v['user']['name']} возраст {v['user']['age']}. Посетил город  {city}.")
	else:
		print("Нет такого города!")
b = float(time.time())
print(f"Парсинг через value(): {(b - a):.20}")
c["value"] = (b - a)

#------------------
print("---------")
a = float(time.time())
try:
	city[0]
except:
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
c["enumerate"] = (b - a)

#---------------------
print("----------")
a = float(time.time())
try:
	city[0]
except:
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
c["iter"] = (b - a)

#------------
print("------------")

a = float(time.time())
if city in cities:
	for i in tourists:
		for key in i:
			if i[key] == city:
				for j in i:
					if j == 'user':
						print(f"Турист {i[j]['name']} возраст {i[j]['age']}. Посетил город {city}.")
else:
	print("Нет такого города...")
b = float(time.time())
print(f"Прямой парсинг словарей из списков: {(b - a):.20}")
c["Прямой"] = (b - a)
print("----------")
print(c)
print("----------")
print("СРАВНЕНИЕ СКОРОСТИ ПО ВОЗРАСТАНИЮ.")
list_c = list(c.items())
list_c.sort(key=lambda i: i[1])
for i in list_c:
	print(i[0], ':', i[1])	
