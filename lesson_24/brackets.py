class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


def check_str(my_str):
    stack = Stack()
    symbols = {
        '"': '"',
        ')': '('
    }
    for symbol in my_str:
        if symbol in symbols.values():
            if symbol == symbols[symbol]:
                try:
                    stack.pop()
                except IndexError:
                    return False
            else:
                stack.push(symbol)
        elif symbol in symbols.keys():
            if symbol == symbols[symbol]:
                try:
                    stack.pop()
                except IndexError:
                    return False
    return True


if __name__ == "__main__":
    a = '"(")'
    b = '(""")'
    print(check_str(a))
    print(check_str(b))
