"""Task 4
The math quiz program

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
and then responds with a message accordingly.
"""

import random

start = 0
stop = 20
while True:
	number_1 = random.randint(start, stop)
	number_2 = random.randint(start, stop)
	operators = ["+", "-", "*", "/", "%", "//"]
	operator = random.choice(operators)
	try:
		result = eval(str(number_1) + operator + str(number_2))
	except ZeroDivisionError:
		continue
	else:
		while True:
			check_result = input(f"Please evaluate the expression: {number_1}{operator}{number_2}=?\nTo exit enter q\n")

			if check_result == 'q':
				exit()
			elif float(check_result) == result:
				print("Ok")
				break
			else:
				print("Error")
