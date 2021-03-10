"""Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for
retrieving elements using square brackets syntax."""


class IterObj:

    def __init__(self, *args):
        self.__iter_obj = [*args]
        self.__start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start >= len(self.__iter_obj):
            raise StopIteration
        start = self.__start
        self.__start += 1
        return self.__iter_obj[start]

    def __getitem__(self, index):
        return self.__iter_obj[index]


def iter_object(obj):
    index = 0
    while True:
        if index >= len(obj):
            break
        from_send = yield obj[index]
        if from_send is not None:
            index = from_send
        else:
            index += 1


if __name__ == '__main__':
    obj = 'abcdefghijklmnop'
    my_obj = IterObj(*obj)
    print(my_obj[8])
    print(my_obj[1])
    print(next(my_obj))
    print(next(my_obj))
    print()

    my_iter = iter_object('0123456789')

    print(next(my_iter))
    print(my_iter.send(5))
    print(next(my_iter))



