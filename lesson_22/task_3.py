"""
This function works only with positive integers

mult(2, 4) == 8
    True
mult(2, 0) == 0
    True
mult(2, -4)
    ValueError("This function works only with positive integers")
"""
from typing import Optional, Union

Result = Union[int, float]


def mult(a: Optional[Result], n: Optional[Result]) -> Optional[Result]:
    if n < 0:
        raise ValueError("This function works only with positive integers")
    if n == 0:
        return n
    return a + mult(a, n - 1)


if __name__ == '__main__':
    print(mult(2, 4))
    print(mult(2, 0))
    print(mult(5, 6))
    print(mult(1.5, 4))
    print(mult(2, -4))
