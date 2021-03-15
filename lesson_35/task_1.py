"""
Practice asynchronous code

Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number.
Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10. You need to get four
lists of results from corresponding functions.

Rewrite the code to use simple functions to get the same results but using a multiprocessing library. Time the
execution of both realizations, explore the results, what realization is more effective, why did you get a result
like this.
"""
import asyncio
import multiprocessing

from lesson_34.task_1 import time_execution


async def factorial(number):
    f = 1
    for i in range(2, number + 1):
        await asyncio.sleep(1)
        f *= i
    print(f"Factorial({number}) = {f}")


async def fibonacci(number):
    a = 0
    b = 1
    if number < 0:
        print("Incorrect input")

    elif number == 0:
        print(f"Fibonacci({number}) = {0}")
    else:
        for i in range(1, number):
            a, b = b, a + b
        print(f"Fibonacci({number}) = {b}")


async def squares(number):
    squares = number * number
    print(f"Squares({number}) = {squares}")


async def cubic(number):
    cubic = number * number * number
    print(f"Cubic({number}) = {cubic}")


@time_execution
async def gather_tasks(number):
    await asyncio.gather(
        factorial(number),
        fibonacci(number),
        squares(number),
        cubic(number))


def factorial_(number):
    f = 1
    for i in range(2, number + 1):
        f *= i
    print(f"Factorial({number}) = {f}")


def fibonacci_(number):
    a = 0
    b = 1
    if number < 0:
        print("Incorrect input")

    elif number == 0:
        print(f"Fibonacci({number}) = {0}")
    else:
        for i in range(1, number):
            a, b = b, a + b
        print(f"Fibonacci({number}) = {b}")


def squares_(number):
    squares = number * number
    print(f"Squares({number}) = {squares}")


def cubic_(number):
    cubic = number * number * number
    print(f"Cubic({number}) = {cubic}")


@time_execution
def run_all_functions(function, numbers):
    with multiprocessing.Pool() as pool:
        pool.map(function, numbers)


if __name__ == '__main__':
    for i in range(10):
        asyncio.run(gather_tasks(i))

    functions = [factorial_, fibonacci_, squares_, cubic_]

    for function in functions:
        run_all_functions(function, range(10))
