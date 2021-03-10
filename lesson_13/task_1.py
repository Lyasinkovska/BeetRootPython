"""
Write a Python program to detect the number of local variables declared in a function.
"""


def abc():
    x = 1
    y = 2
    str1 = 'abc'


def sqrt_numbers(*args):
    return list(map(lambda x: x ** 2, args))


def foo():
    return 'foo'


def count_locals(func):
    return f'Number of local variables in function {func.__name__}: {func.__code__.co_nlocals}'


if __name__ == '__main__':
    print(count_locals(abc))
    print(count_locals(sqrt_numbers))
    print(count_locals(foo))
