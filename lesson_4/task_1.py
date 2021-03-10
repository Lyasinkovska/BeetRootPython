import random
"""The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
The result should be sent back to the user via a print statement.
"""
start = 1
stop = 10
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
