import random

p = 1
r = 1
s = 1
while True:
	print(f'p = {p} \t r = {r} \t s = {s}')
	mylist = ['p', ] * p + ['r', ] * r + ['s', ] * s
	our_combination = random.choice(mylist)
	player_combination = input('input p, r, s for playing. q for finish ')
	if player_combination in {'p', 'r', 's'}:

		if player_combination == 'p':
			s += 1
			if our_combination == 'r':
				print('You won!')
			elif player_combination == our_combination:
				print('it is a draw')
			else:
				print('You lost :(')
		elif player_combination == 'r':
			p += 1
			if our_combination == 's':
				print('You won!')
			elif player_combination == our_combination:
				print('it is a draw')
			else:
				print('You lost :(')
		elif player_combination == 's':
			r += 1
			if our_combination == 'p':
				print('You won!')
			elif player_combination == our_combination:
				print('it is a draw')
			else:
				print('You lost :(')
	elif player_combination == 'q':
		break

import random

win_variants = {
	'R': ['S', ],
	'S': ['P', ],
	'P': ['R', 'K'],
	'K': ['R', 'S'],
}

all_avail_choices = set(win_variants.keys())

stat_variants = {}
for k in win_variants.keys():
	stat_variants[k] = 1

while True:
	print(f'{stat_variants}')

	mylist = []
	for k in stat_variants:
		mylist += [k] * stat_variants[k]

	our_combination = random.choice(mylist)
	player_combination = input('input p, r, s for playing. q for finish ')
	if player_combination in all_avail_choices:
		for win_key in win_variants:
			if player_combination in win_variants[win_key]:
				stat_variants[win_key] += 1

		if our_combination in win_variants[player_combination]:
			print('You won!')
		elif player_combination == our_combination:
			print('it is a draw')
		else:
			print('You lost :(')

	elif player_combination == 'q':
		break