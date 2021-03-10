from typing import List


class MaxBinaryHeap:

    def __init__(self) -> None:
        self.__heap_list: List[int] = [0]
        self.__current_size: int = 0

    @property
    def heap_list(self):
        return self.__heap_list

    @property
    def size(self):
        return self.__current_size

    def percolate_up(self, i) -> None:
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i //= 2

    def percolate_down(self, i) -> None:
        while i * 2 <= self.__current_size:
            max_ch = self.max_child(i)
            if self.heap_list[i] < self.heap_list[max_ch]:
                self.heap_list[i], self.heap_list[max_ch] = self.heap_list[max_ch], self.heap_list[i]
            i = max_ch

    def max_child(self, i) -> int:
        if i * 2 + 1 > self.__current_size:
            return i * 2
        if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def del_max(self) -> int:
        return_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.__current_size]
        self.__current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return return_value

    def build_heap(self, items: List[int]) -> None:
        i = len(items) // 2
        self.__current_size = len(items)
        self.__heap_list = [0] + items[:]
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def insert(self, k) -> None:
        self.heap_list.append(k)
        self.__current_size += 1
        self.percolate_up(self.__current_size)


if __name__ == '__main__':
    my_lst = [1, 50, 2, 6, 60, 4]
    my_heap = MaxBinaryHeap()
    my_heap.build_heap(my_lst)
    print(my_heap.heap_list)
    my_heap.insert(90)
    print(my_heap.heap_list)
    my_heap.del_max()
    print(my_heap.heap_list)
    print(my_heap.size)

