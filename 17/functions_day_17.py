import sys
from enum import IntEnum
from typing import TypeAlias
from queue import PriorityQueue


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


MovementNode: TypeAlias = tuple[int, int, Direction, int]
Grid: TypeAlias = list[list[int]]


def read_file_as_list_of_list_and_filter_empty_lines(filename: str) -> Grid:
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [[int(entry) for entry in list(line)] for line in data.split("\n") if len(line) > 0]


def calculate_possible_movements(data: Grid, position: MovementNode) -> dict[MovementNode, int]:
    row, column, direction, steps_taken = position
    possible_movements = {}
    # up
    if row > 0 and direction is not direction.DOWN:
        if direction is not Direction.UP:
            possible_movements.update({(row - 1, column, Direction.UP, 1): data[row - 1][column]})
        elif steps_taken < 3:
            possible_movements.update({(row - 1, column, Direction.UP, steps_taken + 1): data[row - 1][column]})
    # right
    if column < len(data[0]) - 1 and direction is not direction.LEFT:
        if direction is not Direction.RIGHT:
            possible_movements.update({(row, column + 1, Direction.RIGHT, 1): data[row][column + 1]})
        elif steps_taken < 3:
            possible_movements.update({(row, column + 1, Direction.RIGHT, steps_taken + 1): data[row][column + 1]})
    # down
    if row < len(data) - 1 and direction is not direction.UP:
        if direction is not Direction.DOWN:
            possible_movements.update({(row + 1, column, Direction.DOWN, 1): data[row + 1][column]})
        elif steps_taken < 3:
            possible_movements.update({(row + 1, column, Direction.DOWN, steps_taken + 1): data[row + 1][column]})
    # left
    if column > 0:
        if direction is not Direction.LEFT and direction is not direction.RIGHT:
            possible_movements.update({(row, column - 1, Direction.LEFT, 1): data[row][column - 1]})
        elif steps_taken < 3:
            possible_movements.update({(row, column - 1, Direction.LEFT, steps_taken + 1): data[row][column - 1]})
    return possible_movements


def reverse_path(previous: dict[MovementNode, MovementNode], node: MovementNode) -> list[MovementNode]:
    li = [node]
    n = node
    while previous.get(n, None) is not None:
        n = previous.get(n)
        li.append(n)
    return list(reversed(li))


def dijkstra(data: Grid, start_position: MovementNode, destination: tuple[int, int]) -> int:
    processed = set()
    distances = {}
    previous = {}
    terminal_nodes = set()
    q = PriorityQueue()
    q.put((0, start_position))
    distances.update({start_position: 0})
    while q.qsize() > 0:
        prio, current_position = q.get_nowait()
        if current_position not in processed:
            processed.add(current_position)
            if current_position[0] == destination[0] and current_position[1] == destination[1]:
                terminal_nodes.add(current_position)
            for possible_movement, distance in calculate_possible_movements(data, current_position).items():
                alt = distances.get(current_position) + distance
                if alt < distances.get(possible_movement, sys.maxsize):
                    distances.update({possible_movement: alt})
                    previous.update({possible_movement: current_position})
                    q.put((alt, possible_movement))
    terminal_distances = [distances.get(n) for n in terminal_nodes]
    return min(terminal_distances)


def exercise_1(data: Grid) -> int:
    return dijkstra(data, (0, 0, Direction.UP, 0), (len(data)-1, len(data[0])-1))
