"""
Найти кратчайший маршрут на графе из одной заданной точки в другую
"""


class Node:
    instances = {}

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def __new__(cls, *args, **kwargs):
        name = args[0]
        if name not in cls.instances:
            cls.instances[name] = super().__new__(cls)
        return cls.instances[name]


class Graph:
    def __init__(self):
        self._nodes = []
        self._edges = {}

    def add_node(self, node):
        if node not in self._nodes:
            self._nodes.append(node)
        return self

    def set_edge(self, node1, node2, distance):
        key1 = (node1, node2)
        self._edges[key1] = distance
        key2 = (node2, node1)
        self._edges[key2] = distance
        return self

    def _get_children(self, node):
        children = set()
        for n1, n2 in self._edges:
            if n1 == node:
                children.add(n2)
        return children

    def find_path(self, begin, end):
        queue = [begin]
        node_weight = {begin: 0, }
        while queue:
            current = queue.pop(0)
            for ch in self._get_children(current):
                dist = node_weight[current] + self._edges[(current, ch)]
                if ch in node_weight:
                    if node_weight[ch] > dist:
                        node_weight[ch] = dist
                        queue.append(ch)
                else:
                    node_weight[ch] = dist
                    queue.append(ch)
        queue = [end]
        way = [end]
        while queue:
            current = queue.pop(0)
            for ch in self._get_children(current):
                if node_weight[current] - self._edges[(current, ch)] == node_weight[ch]:
                    queue.append(ch)
                    way.append(ch)
        return way[::-1]


if __name__ == "__main__":
    g1 = Graph()
    g1.add_node(Node('A')).add_node(Node('B')).add_node(Node('C')).add_node(Node('D')).add_node(Node('F'))
    g1.set_edge(Node('A'), Node('B'), 2)
    g1.set_edge(Node('B'), Node('C'), 5)
    g1.set_edge(Node('B'), Node('D'), 3)
    g1.set_edge(Node('C'), Node('D'), 1)
    print(g1.find_path(Node('A'), Node('C')))
