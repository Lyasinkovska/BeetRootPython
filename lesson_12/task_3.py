"""
Fraction

Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) with appropriate
checking and error handling

"""


class Fraction:

    def __init__(self, value: int or float):
        self.value = value
        self._error_message = f'Wrong format, type must be {self.__class__.__name__}'

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(self._error_message)
        return Fraction(self.value + other.value)

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(self._error_message)
        return Fraction(self.value - other.value)

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(self._error_message)
        return Fraction(self.value * other.value)

    def __divmod__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(self._error_message)
        elif other == 0:
            raise ZeroDivisionError("Division by zero is forbidden.")
        return Fraction(self.value / other.value)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(self._error_message)
        return self.value == other.value

    def __ne__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(self._error_message)
        return self.value != other.value

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(self._error_message)
        return self.value < other.value

    def __le__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(self._error_message)
        return self.value <= other.value

    def __gt__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(self._error_message)
        return self.value > other.value

    def __ge__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError(self._error_message)
        return self.value >= other.value

    def __str__(self):
        return f'Fraction result: {self.value}'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    x = Fraction(1 / 2)
    y = Fraction(1 / 4)
    print(x)
    print(y)
    print(Fraction(3 / 4))
    print(x < y, x > y, x <= y, x >= y, x == y, x != y)
    print(Fraction('Hello ' + 'world'))
    print(x + y == 0.75)


