"""
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!

For example:
"add called with 4, 5"

def logger(func):
    pass

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
"""
from functools import wraps


def print_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args)
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        arguments = ", ".join(args_repr + kwargs_repr)
        print(f"{func.__name__} called {arguments}")
        return func

    return wrapper


@print_function
def fibonacci_number(index):
    a, b = 0, 1
    for _ in range(index - 2):
        a, b = b, a + b
    print(f'{index} element of Fibonacci sequence is {b}')
    return 0 if index == 1 else b


@print_function
def square_all(*args):
    return [arg ** 2 for arg in args]


@print_function
def add(x, y):
    return x + y


if __name__ == '__main__':
    fibonacci_number(8)
    square_all(1, 3, 8)
    add(2, 9)
