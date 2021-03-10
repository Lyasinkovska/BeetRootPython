"""
Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method, which will take two
parameters `start` and `stop`, and return a copy of the list starting at the position and going up to but not
including the stop position.
"""

from teachers_node import Node


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def append(self, item):
        """
        adds a new item to the end of the list making it the last item in the collection.
        It needs the item and returns nothing. Assume the item is not already in the list.
        """
        if self._head is None:
            self._head = Node(item)
        else:
            current = self._head
            while current.get_next():
                current = current.get_next()
            current.set_next(Node(item))

    def pop(self):
        """
        removes and returns the last item in the list. It needs nothing and returns an item.
        Assume the list has at least one item.
        """
        current = self._head
        previous = None
        if self.is_empty():
            raise Exception(f"Deleting from empty {self.__class__.__name__}")
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        previous.set_next(None)

    def index(self, item):
        """
        returns the position of item in the list. It needs the item and returns the index.
         Assume the item is in the list.
        """
        current = self._head
        counter = 0
        while current.get_next() is not None:
            if current.get_data() == item:
                return counter
            else:
                counter += 1
                current = current.get_next()
        if current.get_data() == item:
            return counter
        else:
            return -1

    def insert(self, pos, item):
        """
        adds a new item to the list at position pos. It needs the item and returns nothing.
        Assume the item is not already in the list and there are enough existing items to have position pos.
        """
        if pos > self.size() or pos < 0:
            raise AttributeError(f'Cannot insert in {self.__class__.__name__} of length {self.size()}')

        new_node = Node(item)
        current = self._head
        previous = None
        found = False
        counter = 0
        while not found:
            if counter == pos:
                found = True
            else:
                previous = current
                current = current.get_next()
                counter += 1

        if self.size() == pos:
            self.append(new_node)
        elif previous is None:
            new_node.set_next(current)
            self._head = new_node
        elif current.get_next() is None:
            previous.set_next(new_node)
            new_node.set_next(current)
        else:
            previous.set_next(new_node)
            new_node.set_next(current)
            current = new_node

    def slice(self, start: int, stop: int) -> 'UnorderedList':
        """
        take two parameters `start` and `stop`, and return a copy of the list starting at the position and going
        up to but not including the stop position
        """
        sliced_list = UnorderedList()
        if not 0 <= start <= self.size():
            start = 0
        if not 0 <= stop <= self.size():
            stop = self.size()

        counter = 0
        current = self._head
        while stop > counter:
            if counter in range(start, stop):
                sliced_list.append(current)
            current = current.get_next()
            counter += 1
        return sliced_list

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    my_list.add(100)
    my_list.append(1)
    my_list.append(5)
    # print(my_list.size())
    # my_list.pop()
    # print(my_list.size())
    print(my_list)

    my_list.insert(1, 10)
    print(my_list)
    print(my_list.slice(10, 10))

    # print(my_list.index(5))
    # print(my_list.index(6))
    # print(my_list.index(100))
    # print(my_list.search(93))
    # print(my_list.search(100))
    # print(my_list.search(100))
    # print(my_list.size())
    #
    # my_list.remove(54)
    # print(my_list.size())
    # my_list.remove(93)
    # print(my_list.size())
    # my_list.remove(31)
    # print(my_list.size())
    # print(my_list.search(93))
