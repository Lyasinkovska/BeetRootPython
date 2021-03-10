"""
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:

max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise,
return the result.

"""
import functools


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator_arg_rules(func):
        @functools.wraps(func)
        def wrapper_arg_rules(*args, **kwargs):
            string_to_check = args[0]
            check_result = type(string_to_check) == type_ and len(string_to_check) <= max_length and all(
                elem in string_to_check for elem in contains)
            if check_result:
                return func(*args, **kwargs)
            else:
                return check_result

        return wrapper_arg_rules

    return decorator_arg_rules


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    print(create_slogan('johndoe05@gmail.com'))
    print(create_slogan('S@SH05'))

    assert create_slogan('johndoe05@gmail.com') is False
    assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
