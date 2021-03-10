"""
Checks if input string is Palindrome
is_palindrome('mom')
    True
is_palindrome('sassas')
    True
is_palindrome('o')
    True
"""


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) < 2:
        return True
    if looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])


if __name__ == '__main__':
    print(is_palindrome('mom'))
    print(is_palindrome('sassas'))
    print(is_palindrome('o'))
    print(is_palindrome('llappyyppah'))
