"""
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss.

Each Boss has a list of his own
workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances
of Boss class to workers list directly via access to attribute, use getters and setters instead!
You can refactor the existing code.

id_ - is just a random unique integer

"""


class Boss:
    __instances = 0

    def __init__(self, id_: int, name: str, company: str):
        Boss.__instances += 1
        self.id = Boss.__instances
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, worker):
        if isinstance(worker, Worker) and worker not in self.workers and (worker.boss is self or worker.boss is None):
            worker.boss = self
            self._workers.append(worker)
        else:
            raise Exception(f"Change boss for {worker.name} before adding to workers list.")

    @workers.deleter
    def workers(self):
        for w in self.workers:
            if w.boss != self:
                self.workers.remove(w)
                print(f'{w.name} deleted from {self.name} list.')

    def __eq__(self, other):
        return self.name == other.name and self.company == other.company

    def __str__(self):
        return f'{self.name}: {self.workers}'

    def __repr__(self):
        return self.__str__()


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        if not hasattr(self, '_boss'):
            self.boss = ''
        return self._boss

    @boss.setter
    def boss(self, new_boss: Boss):
        if isinstance(new_boss, Boss):
            old_boss = self._boss
            self._boss = new_boss
            del old_boss.workers
        else:
            raise Exception(f"{new_boss} must be instance of {Boss.__name__}")

    @boss.deleter
    def boss(self):
        self._boss = None

    def __eq__(self, other):
        if not isinstance(other, Worker):
            raise NotImplementedError
        return self.id == other.id and self.name == other.name and self.company == other.company

    def __str__(self):
        return f'{self.id}.{self.name}: {self.boss if self.boss is None else self.boss.name}'

    def __repr__(self):
        return f'{self.id}. {self.name}'


if __name__ == '__main__':
    b = Boss(1, 'Olena Teliga', 'SoftServe')
    b2 = Boss(2, 'Ivan Ivanov', 'EPAM')
    b3 = Boss(5, 'Mykola Gonchar', 'Intellias')

    w1 = Worker(1, 'Liudmyla Yasinkovska', 'SoftServe', b)
    w2 = Worker(2, 'Oksana Braun', 'EPAM', b)
    w3 = Worker(3, 'Oleg Green', 'EPAM', b)

    b.workers = w1
    w3.boss = b
    b.workers = w3
    b2.workers = w3
    print(b)
    w3.boss = b2
    b2.workers = w3
    w2.boss = b2
    b2.workers = w2
    print(b)
    print(b2)

