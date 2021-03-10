"""Task 1
The greatest number
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
"""
from random import randint

# 1st option
i = 0
list_of_numbers = list()
while i < 10:
	i += 1
	list_of_numbers.append(randint(0, 100))
print(max(list_of_numbers))

# 2nd option
print(max([randint(0, 100) for _ in range(10)]))
