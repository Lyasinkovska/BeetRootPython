"""
Task 3
Extracting numbers.
Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration
"""
# option 1
list1, list2 = list(range(1, 101)), []
i = 0
while i < len(list1):
	if list1[i] % 7 == 0 and not list1[i] % 5 == 0:
		list2.append(list1[i])
	i += 1
print(list2)

# option 2
print([elem for elem in list(range(1, 101)) if elem % 7 == 0 and elem % 5 != 0])
