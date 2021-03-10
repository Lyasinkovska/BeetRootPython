import random

"""task 1
За 10 попыток получить максимальное рендомное число. 
Количество попыток запрашивать у пользователя."""

while True:
	try:
		max_attempts = int(input("Enter quantity of attempts: "))
		start = int(input("Enter min number: "))
		stop = int(input("Enter max number: "))
		result = None
		while max_attempts > 0:
			number = random.randint(start, stop)
			if result is None or result < number:
				result = number
			max_attempts -= 1
		print(result)
		break
	except ValueError:
		print("You should enter a number!")