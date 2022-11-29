
# План на первый блок
#1. Организовать кодовую базу (создать git-репозиторий)
#2. Установить интепретатор Python >=3.8 (https://www.python.org/downloads/)
#3. Изучить установку внешних пакетов через pip (https://pypi.org/)
#4. Установить Jupyter Notebooks (https://jupyter.org/) — если используете VS Code с Питон-сервером Pylance (входит в состав официального Python расширения), то Jupyter будет встроен в интерактивную среду
#5. Изучить основные типы и структуры данных Питона (списки, словари, кортежи, множества)
#6. Описать предметную область на свой выбор при помощи встроенных типов и структур данных


# Типы данных в Python:

# Artist
name = 'Salvador' #String
surname = 'Dalí' #String
years = [1904, 1989] #List
bornCountry = {'Country': 'Spain', 'City': 'Figueres'} # Dictionaries (словари)
movement = ('Surrealism','Cubism',  'Dada'); # Tuples (кортежи)

print(name + ' ' * 2, surname[:-1],  surname[:2], surname)

# Boolean (логический тип данных)
if years[1]: #True
	print('Dead')
 
if not years[1]:
	print('Alive')
 
# List
fullName = list(name + surname) #List
print(fullName)
print(sorted(fullName), ' ',  fullName)
print(fullName, ' ', fullName.sort(reverse=True))
print('Original:', fullName, 'Pr', fullName[2:4])
print('Original:', fullName, 'Pr', fullName[::-2])

print(sorted(movement))
#movement[1] = 'Realism' # Ошибка "Нельзя изменять элементы кортежа"

print(bornCountry['Country'], bornCountry['City']);

# Sets (множества)
set1 = {surname, 'Пейзаж близ Фигераса', 'Искусство живописи', 1911, 1688, 'Музей Дали'}
set2 = {'Дельфтский', 'Дельфтский', 'Искусство живописи', 1668, surname, 'Музей Нью-Йорка'}
print('Пересечение: ', set1 & set2) 
print('Объединение: ',set1 | set2) 
print('Разность: ',set1 - set2) 
print('Симметрическая разность: ',set1 ^ set2) 
