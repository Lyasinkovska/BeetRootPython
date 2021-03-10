"""task 2
написать цикл получения строки по определенному формату (число)
пока не введет число и мучаем его"""

attempts = 5
while attempts > 0:
	valid_number = input()  # "+38 (098) 614 45 86"
	space_pos = [i for i, symbol in enumerate(valid_number) if symbol == " "]

	if len(valid_number) == 19 and valid_number.startswith("+38") and valid_number.find("(") == 4 and \
		valid_number.find(")") == 8 and valid_number[5] == "0" and space_pos == [3, 9, 13, 16]:
		valid_number = valid_number.strip("+38").replace("(", "").replace(")", "").replace(" ", "")

	if valid_number.isnumeric():
		print("Valid number")
		break
	else:
		attempts -= 1
		print("Invalid number, try again" if attempts > 0 else "No more attempts")