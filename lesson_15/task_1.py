"""
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter
email, passed to the constructor. The logic inside the `validate` method could be to check if the passed email
parameter is a valid email string.
"""
import re


class Validate:

    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if self.check_email(email):
            self._email = email
        else:
            self._email = None
            raise Exception('Wrong email format.')

    @staticmethod
    def check_email(email):
        regex = '^[a-z0-9]+[-._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            return True
        else:
            return False


if __name__ == '__main__':
    my = Validate('g.gg@gmail.com')
    print(my.email)
    # other = Validate('mmm.hh')
    # print(other.email)
