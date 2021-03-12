"""
Primes

We have the following input list of numbers, some of them are prime. You need to create a utility function that takes
as input a number and returns a bool, whether it is prime or not.

Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS.
Compare the results and performance of each of them.
"""
import concurrent.futures
import os
import time
from functools import wraps

NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime

    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]


def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f'{func.__name__} duration: {duration}')
        return result

    return wrapper


def task_id(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing task on process: {os.getpid()}, parent process: {os.getppid()}")
        return func(*args, **kwargs)

    return wrapper


@task_id
def is_prime(number):
    if number == 2 or number == 3:
        return number, True
    if number % 2 == 0 or number < 2:
        return number, False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return number, False
    return number, True


@time_execution
def get_prime_threads(array):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for numb in array:
            try:
                future = executor.submit(is_prime, numb)
            except Exception:
                raise
            else:
                return future.result()


@time_execution
def get_prime_processes(array):
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for numb in array:
            try:
                future = executor.submit(is_prime, numb)
            except Exception:
                raise
            else:
                print(future.result())


if __name__ == '__main__':
    get_prime_processes(NUMBERS)
    get_prime_threads(NUMBERS)
