"""
Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""


def generate_fullname(firstname, lastname, middlename=''):
    return f'{firstname} {middlename + " " if middlename else ""}{lastname}'


def generate_upper_fullname(f_name, l_name, m_name=''):
    return generate_fullname(f_name, l_name, m_name).upper()


def create_invitation(func):
    def invitation(f_name, l_name, middle=''):
        return f'Hello dear, {func(f_name, l_name, middle)}. Were are happy to see you here.'

    return invitation


if __name__ == '__main__':
    my_name = create_invitation(generate_fullname)
    my_upper_name = create_invitation(generate_upper_fullname)
    print(my_name('Liudmyla', 'Yasinkovska'))
    print(my_upper_name('Liudmyla', 'Yasinkovska'))
