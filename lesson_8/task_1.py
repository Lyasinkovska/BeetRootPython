"""
Write a function called oops that explicitly raises an IndexError exception when called. Then write another function
that calls oops inside a try/except statement to catch the error. What happens if you change oops to raise KeyError
instead of IndexError?
"""


def oops_index_error():
    raise IndexError


def oops_key_error():
    raise KeyError


def another_function():
    names = {'Liuda': 1, "Vasya": 2}
    try:
        print(names['Kolya'])
        print("No IndexErrors")
    except:
        oops_index_error()


another_function()
