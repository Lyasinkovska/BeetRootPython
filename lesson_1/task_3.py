"""Task 3
Write a program, which has two print statements to print the following text (capital letters “O” and “H”, made from “#”
symbols):

#########
#       #
#       #
#       #
#########

#       #
#       #
#########
#       #
#       #
Pay attention that usage of spaces is forbidden, as well as creating the whole result text
string using “”” ”””, use ‘\n’ and ‘\t’ symbols instead.
"""


print('#'*9, '#\t\t#', '#\t\t#', '#\t\t#', '#'*9, sep='\n', end='\n'*2)
print('#\t\t#', '#\t\t#','#'*9, '#\t\t#', '#\t\t#', sep='\n')