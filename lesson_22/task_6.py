""""
def sdvig(inval: int,  num: int = 1) -> int:
   pass

assert sdvig(123) == 312
assert sdvig(120) == 12
assert sdvig(120, 2) == 201
assert sdvig(543210, 3) == 210543
"""


def tens_in_number(number: int) -> int:
    tens = 0
    while number > 9:
        number = number // 10
        tens += 1
    return tens


def digits_shift(number: int, step: int = 1) -> int:
    tens = tens_in_number(number)
    if number < 10:
        return number

    while step:
        number = (number % 10) * (10 ** tens) + number // 10
        step -= 1
    return number


def digits(number, step=1):
    tens = tens_in_number(number)
    print(number)
    if number < 10:
        return number

    return (number % 10) * (10 ** tens) + digits(number // 10, step-1)


if __name__ == '__main__':
    # print(digits_shift(10002))
    # print(digits_shift(10002, 4))
    # assert digits_shift(1) == 1
    # assert digits_shift(123) == 312
    # assert digits_shift(120) == 12
    # assert digits_shift(120, 2) == 201
    # assert digits_shift(543210, 3) == 210543
    # print(digits(123, 3))
    print(tens_in_number(100))
