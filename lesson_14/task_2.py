"""
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

"""
from functools import wraps


def stop_words(words: list):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            new_str = func(*args, **kwargs)
            for word in words:
                new_str = new_str.replace(word, '*')
            return new_str

        return inner

    return wrapper


@stop_words(['pepsi', 'BMW', 'Hohoho'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    print(create_slogan('Hanna'))
    assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
