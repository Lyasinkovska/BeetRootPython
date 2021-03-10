"""
from typing import Optional
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    Returns  x ^ exp
to_power(2, 3) == 8
    True
to_power(3.5, 2) == 12.25
    True
to_power(2, -1)
    ValueError: This function works only with exp > 0.

"""
from typing import Optional, Union

Result = Union[int, float]


def to_power(x: Optional[Result], exp: int) -> Optional[Result]:
    if exp < 0:
        raise ValueError('This function works only with exp > 0')
    if exp == 1:
        return x
    return x * to_power(x, exp - 1)


if __name__ == '__main__':
    print(to_power(2, 3))
    print(to_power(3.5, 2))
    print(to_power(2, 12))
    print(to_power(2, -1))
