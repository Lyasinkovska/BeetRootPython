"""task 3
получить от пользователя 10 чисел и вывести максимальное
"""
attempts = 10
max_number = None
while attempts > 0:
	try:
		number = int(input("Enter any number: "))
		if max_number is None or max_number < number:
			max_number = number
		attempts -= 1
	except ValueError:
		print("You should enter a numerical value!")
print(max_number)