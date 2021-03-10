"""
Для вводимых пользователем чисел отбираем минимальное и максимальное.
"""
max_attempts = 5
max_number = None
min_number = None
while max_attempts > 0:
	user_input = input("Enter any number: ")
	if user_input.isdigit():
		if max_number is None or max_number < int(user_input):
			max_number = int(user_input)
		if min_number is None or min_number > int(user_input):
			min_number = int(user_input)
		max_attempts -= 1
	elif user_input == "Q":
		break
	else:
		print("Wrong format, try again.")
		continue

print(f"Maximum number: {max_number}, minimum number: {min_number}" if max_number \
	else "You haven't entered any numbers.")
