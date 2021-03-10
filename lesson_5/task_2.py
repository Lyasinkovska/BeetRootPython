"""
Task 2
Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 100, and make a third list containing the common
integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers

"""
from random import randint

# option 1
list1, list2, list3 = [randint(0, 100) for _ in range(10)], [randint(0, 100) for _ in range(10)], []
i = 0
while i < 10:
	if list1[i] in list2:
		list3.append(list1[i])
	i += 1
print(list3 if list3 else "No duplicates.")

# option 2
print(set(list1) & set(list2))
# print(set(list1) | set(list2))
# print(set(list1) - set(list2))
