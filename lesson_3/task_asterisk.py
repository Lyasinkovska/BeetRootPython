import random

"""task 1
Получить от пользователя его номер телефона, проверить подходит ли номер под форматы
+380_________ (прочерки - любая цифра)
0_________ (например 0931233232)
0__ ___ __ __ (пробелы именно пробелы и телефон например 095 321 12 21)
Если номер введен верно - похвалите человека. Если нет - поругайте."""

test_numbers = ["+380986455862", "0986455862", "098 645 5862", "098645 58_62",
				"098 645  862", "098 645__662", "098 645 b862", "325 698 55 66"]

while True:
	number = (input("Please, enter your phone number in the following format:\n")).strip()

	if number.startswith("+380"):
		number = number.strip("+380")
	elif number.startswith("0"):
		number = number[1:].replace(" ", "")

	if number.isnumeric() and len(number) == 9:
		print("The number is correct.")
		break
	else:
		print("The number format is wrong. Please try again.")

"""задание 3
проверить что введенная строка является полиндромом."""

word = input("Enter a word: ")
print("It is a palindrome." if word.lower() == word[::-1].lower() else "It is not a palindrome.")


"""Задание (із зірочкой):
Задание 2 пример по математике просто решить глядя в код, а что если переменную инициализировать случайным значением?
В первой строке импортируйте модуль рандома
import random
обьявите переменные (случайное целое от 1 до 20 включительно)
var1 = random.randint(1,20)
Теперь сделайте задание 2 но уже со случайными значениями.
"""


def evaluation(number1, number2, operator):
	if operator == "+":
		return number1 + number2
	elif operator == "-":
		return number1 - number2
	elif operator == "*":
		return number1 * number2


number_1 = random.randint(1, 20)
number_2 = random.randint(1, 20)
operators = ["+", "-", "*"]
operator = random.choice(operators)
result = evaluation(number_1, number_2, operator)
check_result = int(input(f"Please evaluate the expression: {number_1}{operator}{number_2}=?\n"))
if check_result == result:
	print("Ok")
else:
	print("Error")


"""Завдання 4: програма загадує число у вказаному діапазоні, а юзер повинен його вгадати."""

start = int(input("Please, enter start number:\n"))
stop = int(input("Please, enter stop number:\n"))
number = random.randint(start, stop)
while True:
	try:
		user_number = int(input(f"Try to guess number in the range ({start}, {stop})\n"))
	except ValueError:
		print("Your guess must be a number.")
	else:
		if user_number < start or user_number > stop:
			print("You are out of range")
			continue
		elif user_number == number:
			print("Excellent. You are the winner!")
			break
		elif number > user_number:
			print(f"The number is greater than {user_number}")
		elif number < user_number:
			print(f"The number is less than {user_number}")
