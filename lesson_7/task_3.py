"""
A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the
second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42
"""
from lesson_4.task_5_4 import add, subtract, multiply


def make_operation(operator, total, *args):
    """
    takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
    and an arbitrary number of arguments (only numbers) as the second parameter
    :type total: int
    :param operator:
    :param args:
    :return: the sum or product of all the numbers in the arbitrary parameter
    """
    action = get_action(operator)
    if action is None:
        return "The function cannot calculate it."
    else:
        for number in args:
            total = action(total, number)
        return total


def get_action(action):
    """
    Takes the operator as parameter and return the arbitrary function.
    :param action:
    """
    actions = {"+": add, "-": subtract, "*": multiply}
    if action in actions.keys():
        return actions[action]
    elif action not in actions.keys():
        return None


if __name__ == '__main__':
    print(make_operation("+", 7, 7, 2))
    print(make_operation("-", 5, 5, -10, -20))
    print(make_operation("*", 6, 7))
