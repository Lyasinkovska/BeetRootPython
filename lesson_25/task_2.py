"""
Read about the Fibonacci search and implement it using python. Explore its complexity and compare it to sequential, binary searches.
"""


def fibonacci_search(collection, value):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2
    while fib_m < len(collection):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
        fib_m = fib_m_minus_1 + fib_m_minus_2
    index = -1

    while fib_m > 1:
        i = min(index + fib_m_minus_2, (len(collection) - 1))
        if collection[i] < value:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            index = i
        elif collection[i] > value:
            fib_m = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
        else:
            return i
    if fib_m_minus_1 and index < (len(collection) - 1) and collection[index + 1] == value:
        return index + 1
    return -1
