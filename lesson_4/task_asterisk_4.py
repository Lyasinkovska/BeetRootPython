"""пишем в цикле решение уравнения аХ**2+bx+c=0 рассчитываем ответ. """

while True:
	try:
		print("To exit press Q")
		a = input("enter a: ")
		b = input("enter b: ")
		c = input("enter c: ")
		if a == "Q" or b == "Q" or c == "Q":
			break
		else:
			a, b, c  = map(int, [a, b, c])
			d = b **2 - 4 * a * c
			if d < 0:
				print("No results.")
			elif d == 0:
				x1 = round(-b / (2 * a), 2)
				x2 = x1
				print(f"x1 = {x1}, x2 = {x2}")
			elif d > 0:
				x1 = round((-b + d**0.5) / (2 * a), 2)
				x2 = round((-b - d ** 0.5) / (2 * a), 2)
				print(f"x1 = {x1}, x2 = {x2}")

	except ValueError:
		print("Wrong  format.")