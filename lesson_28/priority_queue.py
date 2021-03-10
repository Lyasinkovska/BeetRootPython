from typing import List


class Task:
    def __init__(self, task: str, priority: int = 0) -> None:
        self.__task = task
        self.__priority = priority

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, new_prior: int) -> None:
        self.__priority = new_prior

    def __repr__(self):
        return f'{self.__priority} - {self.__task}'


class PriorityQueue:
    def __init__(self):
        self.__prior_queue: List[Task] = [Task('', 0)]
        self.__size: int = 0

    @property
    def priority_queue(self):
        return self.__prior_queue

    def __len__(self):
        return self.__size

    def __perc_up(self, i) -> None:
        while i // 2 > 0:
            if self.__prior_queue[i].priority < self.__prior_queue[i // 2].priority:
                self.__prior_queue[i // 2], self.__prior_queue[i] = self.__prior_queue[i], self.__prior_queue[i // 2]
            i //= 2

    def __perc_down(self, i) -> None:
        while (i * 2) <= self.__size:
            mc = self.__min_child(i)
            if self.__prior_queue[i].priority > self.__prior_queue[mc].priority:
                self.__prior_queue[i], self.__prior_queue[mc] = self.__prior_queue[mc], self.__prior_queue[i]
            i = mc

    def __min_child(self, i) -> int:
        if i * 2 + 1 > self.__size:
            return i * 2
        if self.__prior_queue[i * 2].priority < self.__prior_queue[i * 2 + 1].priority:
            return i * 2
        else:
            return i * 2 + 1

    def enqueue(self, task: Task) -> None:
        self.__prior_queue.append(task)
        self.__size += 1
        self.__perc_up(self.__size)

    def dequeue(self):
        ret_val = self.__prior_queue[1]
        self.__prior_queue[1] = self.__prior_queue[self.__size]
        self.__size -= 1
        self.__prior_queue.pop()
        self.__perc_down(1)
        return ret_val

    def __repr__(self):
        return self.__prior_queue[1:]

    def __str__(self):
        return f'{self.__repr__()}'


if __name__ == '__main__':
    my_queue = PriorityQueue()
    my_queue.enqueue(Task('wash dishes', 1))
    my_queue.enqueue(Task('do homework for Python course', 10))
    my_queue.enqueue((Task('clean up the house', 5)))
    my_queue.enqueue(Task('sleep', 6))
    my_queue.enqueue(Task('walk with the dog', 9))
    print(my_queue.priority_queue)
    print(my_queue.dequeue())
    print(len(my_queue))
    print(my_queue.priority_queue)
