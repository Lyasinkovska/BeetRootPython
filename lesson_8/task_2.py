"""
Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block which raises an exception
if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).
"""


def square_division_of_two_numbers(first_elem, second_elem):
    try:
        first_elem, second_elem = map(int, (first_elem, second_elem))
    except ZeroDivisionError:
        return "Division by zero is forbidden."
    except ValueError:
        return 'ValueError: could not convert string to integer.'


if __name__ == '__main__':
    a, b = input('enter a: '), input('enter b: ')
    print(square_division_of_two_numbers())
