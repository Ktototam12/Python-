"""Стандарты оформления Python-модулей
PEP8
области видимости
классы
переменные [глобальные, локальные, вложенные]
"""

# Определены вне функции. Глобальные переменные: константа и переменная
INIT_FACT_GLOBAL_CONST = 1
test_global = 1234

def fact(x : int) -> int:
	"""Вычислить факториал числа x """
	return fact(x - 1) * x if x > INIT_FACT_GLOBAL_CONST else INIT_FACT_GLOBAL_CONST

def foo(x : int) -> int:
	"""Показывает области видимости в функциях """
	x = 1
	def boo():
     	# Локальная boo
		x = 2 
	boo()
	return x

def foo1(x : int) -> int:
	"""Показывает области видимости в функциях """
	x = 1
	def boo1(): 
     	# Позволяет связывать ранее объявленную переменную вне локальной области boo, кроме глобальной области
		nonlocal x 
		x = 2
	boo1()
	return x

def foo2():
	""" Показывает области видимости в функциях """
      	# Внутри функции создается глобальная переменная, видимая из любого места
	global test_global
	test_global = 4321

if __name__ == '__main__':
	""" Главная функция лр2 """
	print(fact(2)) 
 # выведет 1, несмотря на то, что в boo() присваивается 2
	print(foo(10)) 
 # выведет 2, так как в boo1 nonlocal x
	print(foo1(10)) 
	print(test_global)
	foo2()
	print(test_global)
