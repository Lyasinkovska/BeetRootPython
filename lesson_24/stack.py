class Stack:
    def __init__(self):
        self._items = []

    @property
    def is_empty(self):
        return not len(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]


    def __repr__(self):
        representation = "<Stack>\n"
        # for ind, item in enumerate(reversed(self._items), 1):
        #     representation += f"{ind}: {str(item)}\n"
        return representation + f"{self._items}"

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self._items)


if __name__ == "__main__":
    s = Stack()

    print(s.is_empty)
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s)
    print(s.pop())
    print(s)
