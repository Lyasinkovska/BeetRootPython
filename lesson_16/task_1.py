"""
Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function
"""
from typing import Iterable


def with_index(sequence, start=0):
    if isinstance(sequence, Iterable):
        for elem in sequence:
            yield start, elem
            start += 1
    else:
        raise Exception("First parameter must be iterable.")


if __name__ == '__main__':
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for el in with_index(months, start=1):
        print(el)
    number = 123
    for el in with_index(number, start=1):
        print(el)
