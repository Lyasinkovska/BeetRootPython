"""
Implement a queue using a singly linked list.
"""
from typing import Any

from lesson_24.teachers_node import Node


class Queue:

    def __init__(self) -> None:
        self.__size = 0
        self.__front = None
        self.__rear = None

    @property
    def data(self) -> tuple:
        return self.__rear, self.__front

    @property
    def size(self) -> int:
        return self.__size

    @property
    def is_empty(self) -> bool:
        return not self.__size

    def enqueue(self, item: Any) -> None:
        new_item = Node(item)
        if self.__rear is None:
            self.__front = self.__rear = new_item
        else:
            new_item.set_next(self.__rear)
            self.__rear = new_item
        self.__size += 1

    def dequeue(self) -> None:
        if self.is_empty:
            raise Exception(f'{self.__class__.__name__} is empty.')
        if self.__rear == self.__front:
            self.__rear = self.__front = None
        else:
            current = self.__rear
            while current.get_next() != self.__front:
                current = current.get_next()
            self.__front = current
        self.__size -= 1

    def __repr__(self) -> str:
        representation = "|Queue: "
        current, last = self.__rear, self.__front
        if current is not None and last is not None:
            while current != last:
                representation += f"{current.get_data()} "
                current = current.get_next()
            representation += f'{last.get_data()}'
        return f'{representation}|'


if __name__ == '__main__':
    my_q = Queue()
    print(my_q)
    my_q.enqueue(5)
    print(my_q)
    print(my_q.size)
    my_q.dequeue()
    print(my_q.size)

    my_q.enqueue(6)
    my_q.enqueue('Hello')
    my_q.enqueue(True)
    print(my_q)
