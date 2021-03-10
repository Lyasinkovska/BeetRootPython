"""камень-ножницы-бумага пока не надоест (Q) загадываем и спрашиваем пользователя что он загадал.
Плюсуем себе или ему победу и так по кругу. Принтуем общий счет.
"""
import random

game_elements = ["rock", "scissors", "paper"]
comp_counter = 0
user_counter = 0
while True:
	computer_choice = random.choice(game_elements)
	user_input = input("Choose and enter number: \n1.rock, 2.scissors, 3.paper\n> ")

	if user_input == "Q":
		break
	elif user_input in ["1", "2", "3"]:
		comp_win = False
		user_choice = game_elements[int(user_input) - 1]
		print(f"Computer: {computer_choice}, User: {user_choice}")
		if computer_choice == user_choice:
			print("Draw.")
			continue

		if computer_choice == "rock":
			if user_choice == "scissors":
				comp_counter += 1
				comp_win = True
			elif user_choice == "paper":
				user_counter += 1
		elif computer_choice == "scissors":
			if user_choice == "rock":
				user_counter += 1
			elif user_choice == "paper":
				comp_counter += 1
				comp_win = True
		elif computer_choice == "paper":
			if user_choice == "rock":
				comp_counter += 1
				comp_win = True
			elif user_choice == "scissors":
				user_counter += 1

			if computer_choice:
				print(f"Computer wins.")
			else:
				print("You win.")
	else:
		print("Please choose correct option!")
		continue

print(f"Computer vs User ({comp_counter}:{user_counter}).")
