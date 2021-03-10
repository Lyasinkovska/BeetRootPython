"""
The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message
like this:

     “Good day <name>! <day> is a perfect day to learn some python.”
Note that <name> and <day> are predefined variables in source code.
An additional bonus will be to use different string formatting methods for constructing result string.
"""

name = "Liuda"
day = "Friday"
print(f"Good day {name}! {day} is a perfect day to learn some python.")
print("Good day {}! {} is a perfect day to learn some python.".format(name, day))
print("Good day {1}! {0} is a perfect day to learn some python.".format(day, name))
print("Good day {name}! {day} is a perfect day to learn some python.".format(name = "Liuda", day = "Friday"))

empty_l = []
empty_l.append(empty_l)

print(empty_l)
print(empty_l.copy())

