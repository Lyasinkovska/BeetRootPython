"""
Write a program that reads in a sequence of characters and prints them in reverse order,
using your implementation of Stack.
"""
from collections import deque


def print_reversed_string(chars: str = '') -> None:
    if not isinstance(chars, str):
        try:
            chars = str(chars)
        except TypeError:
            raise TypeError("Input must be string")

    my_stack = deque()
    reversed_string = ''
    for char in chars:
        my_stack.append(char)
    while my_stack:
        reversed_string += my_stack.pop()
    print(reversed_string)


if __name__ == '__main__':
    print_reversed_string('Hello my dear friend.')
    print_reversed_string(123)
    print_reversed_string([1, 5, 8])
