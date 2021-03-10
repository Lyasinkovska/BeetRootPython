"""
Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
`start`, `end`, and optional step. Tips: See the documentation for `range` function
"""


class InRange:
    def __init__(self, start: int, stop: int, step: int = 1):
        self.__start = start
        self.__stop = stop
        self.__step = step
        self.__range = []

    @property
    def range(self):
        return self.__range

    def __iter__(self):
        return self

    def is_valid_arguments(self):
        if not all(isinstance(arg, int) for arg in (self.__start, self.__stop, self.__step)):
            raise TypeError('Arguments must be integers')
        return True

    def __next__(self):
        if self.is_valid_arguments():
            if self.__step > 0 and self.__start >= self.__stop or (self.__step < 0 and self.__start <= self.__stop):
                raise StopIteration

            if self.__step == 0:
                raise ValueError("Step cannot be 0")
            current = self.__start
            self.__start += self.__step
            self.__range.append(current)
            return current

    def __contains__(self, item):
        return item in self.__range


if __name__ == '__main__':
    my_range = InRange(1, 13, 2)
    for i in my_range:
        print(i)
    print(my_range.range)
    print(5 in my_range)
    print(2 in my_range)

#
#
# class InRange:
#     def __init__(self, *args: int):
#         self.__arguments = args
#         self.__start = 0
#         self.__step = 1
#         self.check_type()
#         self.__result = list(self.check_arguments())
#
#     def check_type(self):
#         if not any(isinstance(arg, int) for arg in self.__arguments):
#             raise TypeError('Must be integer')
#
#     def check_arguments(self):
#
#         if len(self.__arguments) == 1 and self.__arguments[0] > 0:
#             self.__stop = self.__arguments[0]
#         elif len(self.__arguments) == 2 and self.__arguments[0] < self.__arguments[1]:
#             self.__start = self.__arguments[0]
#             self.__stop = self.__arguments[1]
#         elif (len(self.__arguments) == 3 and self.__arguments[0] < self.__arguments[1] and self.__arguments[2] > 0) or (
#             len(self.__arguments) == 3 and self.__arguments[0] > self.__arguments[1] and self.__arguments[2] < 0):
#             self.__start = self.__arguments[0]
#             self.__stop = self.__arguments[1]
#             self.__step = self.__arguments[2]
#         else:
#             raise Exception("Wrong arguments")
#         return self.__start - self.__step, self.__stop, self.__step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__result[0] > self.__result[1]:
#             while self.__result[0] + self.__result[2] > self.__result[1]:
#                 self.__result[0] += self.__result[2]
#                 return self.__result[0]
#         elif self.__result[0] < self.__result[1]:
#             while self.__result[0] + self.__result[2] < self.__result[1]:
#                 self.__result[0] += self.__result[2]
#                 return self.__result[0]
#         raise StopIteration
#
#
# if __name__ == '__main__':
#     my = InRange(110, 15, -10)
#     for i in range(2):
#         print(next(my))
#     for i in my:
#         print(i)
#
#     new_range = InRange(5)
#     for i in new_range:
#         print(i)
