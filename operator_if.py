# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:52:46 2020

@author: lukin
"""

cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[0]},
            {'user': users[1], 'city': cities[1]},
            {'user': users[2], 'city': cities[2]}]

city = input('Введите город: ')
#приводим переменную 'city' к виду
#переменных в списке, т.е. обрезаем
#пробелы и переводим первую букву
#к верхнему регистру
city = city.strip().capitalize()

"""
РЕШЕНИЕ ЗАДАЧИ ПРЯМЫМ РАСПАРСИВАНИЕМ СЛОВАРЕЙ ИЗ СПИСКА
с благодарностью к коллеге Ernest, который указал мне, что прямой парсинг
не самый эффективный и быстрый способ получения данных, я решил поискать
другие способы получения данных из конструкций подобных tourists.
Что из этого получилось, смотрите ниже.
"""
print('____________________')
print('РЕШЕНИЕ ЗАДАЧИ ПРЯМЫМ РАСПАРСИВАНИЕМ СЛОВАРЕЙ ИЗ СПИСКА')
try:
    #проверяем введено ли значение
    city[0]
except IndexError:
    #если значение не введено
    print('Вы забыли ввести город!')
#ДАЛЬШЕ ЕСЛИ ЗНАЧЕНИЕ ВВЕДЕНО
else:
#проверяем переменную 'city' 
#на вхождение в список 'cities'
#если нет, то падаем в блок 'else'
    if city in cities:
	#если да, то начинаем работать со
	#списком словарей 'tourists'
	    for i in tourists:
		#перебираем ключи словарей
		    for key in i:
			#если ключ словаря равен
			#значению нашей переменной
			#city, то распарсиваем этот словарь
			    if i[key] == city:
				    for j in i:
					    if j == 'user':
						    #выводим конечное сообщение
						    print("Турист {} возраст {}. Посетил город {}".format(i[j]['name'], i[j]['age'], city))
    else:
        print("Нет такого города...")
        
"""
ПАРСИНГ ЧЕРЕЗ VALUE()
"""
print('____________________')
print('РЕШЕНИЕ ЗАДАЧИ РАСПАРСИВАНИЕМ СЛОВАРЕЙ ИЗ СПИСКА ЧЕРЕЗ VALUE()')
try:
    city[0]
except IndexError:
    print('Вы забыли ввести город!')
else:
    if city in cities:
        for v in tourists:
            if city in v.values():
                print(f"Турист {v['user']['name']} возраст {v['user']['age']}. Посетил город {city}")
    else:
        print('Нет такого города...')
        
"""
ПАРСИНГ ЧЕРЕЗ ENUMERATE()
"""
print('____________________')
print('РЕШЕНИЕ ЗАДАЧИ РАСПАРСИВАНИЕМ СЛОВАРЕЙ ИЗ СПИСКА ЧЕРЕЗ ENUMERATE()')
try:
    city[0]
except IndexError:
    print('Вы забыли ввести город!')
else:
    if city in cities:
        for k, v in enumerate(tourists):
            if city in v['city']:
                print(f"Турист {v['user']['name']} возраст {v['user']['age']}. Посетил город {city}")
    else:
        print('Нет такого города...')
        
"""
ПАРСИНГ ЧЕРЕЗ ITER()
"""
print('____________________')
print('РЕШЕНИЕ ЗАДАЧИ РАСПАРСИВАНИЕМ СЛОВАРЕЙ ИЗ СПИСКА ЧЕРЕЗ ITER()')
try:
    city[0]
except IndexError:
    print('Вы забыли ввести город!')
else:
    if city in cities:
        for v in iter(tourists):
            if city in v['city']:
                print(f"Турист {v['user']['name']} возраст {v['user']['age']}. Посетил город {city}")
    else:
        print('Нет такого города...')
        
print('____________________')
        
