from collections import deque


class Horse:

    def __init__(self, x: int = 0, y: int = 0, dist: int = 0):
        self.x = x
        self.y = y
        self.dist = dist
        self.visited_cells = []
        self.possible_steps = [(2, 1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (2, -1)]

    @property
    def current_position(self):
        return self.x, self.y

    def __repr__(self):
        return f'({self.x}, {self.y}): {self.dist}'


class Board:

    def __init__(self, size: int = 8):
        self.size = size

    def is_valid(self, position):
        return 1 <= position[0] <= self.size and 1 <= position[1] <= self.size

    def shortest_way(self, figure, destination):
        queue = deque()
        queue.append(figure)

        while queue:

            current = queue[0]
            queue.popleft()

            if current.current_position == destination:
                return current.dist

            for step in figure.possible_steps:
                next_position = current.x + step[0], current.y + step[1]

                if self.is_valid(next_position) and self.is_valid(destination) and next_position not in figure.visited_cells:
                    figure.visited_cells.append(next_position)
                    queue.append(Horse(next_position[0], next_position[1], current.dist + 1))


if __name__ == '__main__':
    horse = Horse(1, 1)
    board = Board()
    print(board.shortest_way(horse, destination=(8, 8)))
