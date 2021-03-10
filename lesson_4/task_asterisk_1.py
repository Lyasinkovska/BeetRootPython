"""Спросили у пользователя предел и от нуля до предела выводим(принтуем) все числа кроме кратных 18ти.
На числе 42 принтуем "Потому что".  Числа от 50ти до 80ти игнорируем."""
try:
	max_number = int(input("Enter max_number: "))
	for i in range(max_number):
		if (i == 0 or not i % 18 == 0) and not (50 < i < 80):
			if i == 42:
				print("Потому что")
			else:
				print(i)
except ValueError:
	print("Wrong format.")
