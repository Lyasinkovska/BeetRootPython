"""
Пока пользователь не введет Q но не больше 5 раз запрашиваем у пользователя число.
В конце принтуем максимальное введенное. Если введет не число попытка ввода НЕ засчитывается.
"""
max_attempts = 5
max_number = None
while max_attempts > 0:
	user_input = input("Enter any number: ")
	if user_input.isnumeric():
		if max_number is None or max_number < int(user_input):
			max_number = int(user_input)
		max_attempts -= 1
	elif user_input == "Q":
		break
	else:
		print("Wrong format, try again.")
		continue

print(f"Maximum number: {max_number}" if max_number else "You haven't entered any numbers.")
