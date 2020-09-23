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
try:
    #проверяем введено ли значение
    city[0]
except IndexError:
    #если значение не введено
    print('Вы забыли ввести город!')
#ДАЛЬШЕ ЕСЛИ ЗНАЧЕНИЕ ВВЕДЕНО
else:
#приводим переменную 'city' к виду
#переменных в списке, т.е. обрезаем
#пробелы и переводим первую букву
#к верхнему регистру
    city = city.strip().capitalize()

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
