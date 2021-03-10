"""
Implement a stack using a singly linked list.
"""
from typing import Any

from teachers_node import Node


class Stack:
    def __init__(self) -> None:
        self.__head = None
        self.__size = 0

    @property
    def size(self) -> int:
        return self.__size

    @property
    def is_empty(self) -> bool:
        return not self.__size

    def push(self, item: Any) -> None:
        new_item = Node(item)
        if self.is_empty:
            self.__head = new_item
        else:
            new_item.set_next(self.__head)
            self.__head = new_item
        self.__size += 1

    def pop(self) -> Any:
        if self.is_empty:
            raise Exception(f"Trying to pop from empty {self.__class__.__name__}")
        pop_item = self.__head
        self.__head = pop_item.get_next()
        self.__size -= 1
        return pop_item

    def peek(self) -> Any:
        return None if self.is_empty else self.__head.get_data()

    def __repr__(self) -> str:
        class_name = f'{self.__class__.__name__}: '
        current = self.__head
        while current is not None:
            class_name += f'{current.get_data()} '
            current = current.get_next()
        return class_name

    def __str__(self) -> str:
        return self.__repr__()


if __name__ == '__main__':
    my_stack = Stack()
    print(my_stack.is_empty)
    print(my_stack.peek())
    print(my_stack.size)
    my_stack.push(10)
    print(my_stack.size)
    my_stack.push(11)
    print(my_stack)
    print(my_stack.peek())
    print(my_stack)
    print(my_stack.pop())
    print(my_stack.size)
