"""
Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces,
and curly brackets are "balanced."
"""
from collections import deque


def check_balanced_braces(chars: str = '') -> bool:
    queue = deque()
    open_brackets = '({'
    close_brackets = ')}'
    for char in chars:
        if char in open_brackets:
            queue.append(char)
        elif char in close_brackets:
            try:
                queue.pop()
            except IndexError:
                return False
    return True


if __name__ == '__main__':
    examples = '((1+2)/8)', '(1+2))', "{'1': 1}}", ')(', '(((()()))())'
    for item in examples:
        print(check_balanced_braces(item))
