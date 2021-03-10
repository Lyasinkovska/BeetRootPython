"""
sum_of_digits('26') == 8
    True
sum_of_digits('test')
    ValueError("input string must be digit string")
"""


def sum_of_digits(digit_string: str) -> int:
    try:
        digit_string = int(digit_string)
    except ValueError:
        raise ValueError("input string must be digit string")
    if digit_string < 10:
        return digit_string
    a, b = digit_string % 10, digit_string // 10
    b += sum_of_digits(str(a))
    return sum_of_digits(str(b))


if __name__ == '__main__':
    print(sum_of_digits('26'))
    print(sum_of_digits('999'))
    print(sum_of_digits('789'))
    print(sum_of_digits('test'))
