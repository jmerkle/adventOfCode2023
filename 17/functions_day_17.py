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
    if column > 0 and direction is not direction.RIGHT:
        if direction is not Direction.LEFT:
            possible_movements.update({(row, column - 1, Direction.LEFT, 1): data[row][column - 1]})
        elif steps_taken < 3:
            possible_movements.update({(row, column - 1, Direction.LEFT, steps_taken + 1): data[row][column - 1]})
    return possible_movements


def calculate_possible_movements_ultra(data: Grid, position: MovementNode) -> dict[MovementNode, int]:
    row, column, direction, steps_taken = position
    possible_movements = {}
    # up
    if row > 0 and direction is not direction.DOWN:
        if direction is not Direction.UP and (steps_taken > 3 or steps_taken == 0):
            possible_movements.update({(row - 1, column, Direction.UP, 1): data[row - 1][column]})
        elif direction is Direction.UP and steps_taken < 10:
            possible_movements.update({(row - 1, column, Direction.UP, steps_taken + 1): data[row - 1][column]})
    # right
    if column < len(data[0]) - 1 and direction is not direction.LEFT:
        if direction is not Direction.RIGHT and (steps_taken > 3 or steps_taken == 0):
            possible_movements.update({(row, column + 1, Direction.RIGHT, 1): data[row][column + 1]})
        elif direction is Direction.RIGHT and steps_taken < 10:
            possible_movements.update({(row, column + 1, Direction.RIGHT, steps_taken + 1): data[row][column + 1]})
    # down
    if row < len(data) - 1 and direction is not direction.UP:
        if direction is not Direction.DOWN and (steps_taken > 3 or steps_taken == 0):
            possible_movements.update({(row + 1, column, Direction.DOWN, 1): data[row + 1][column]})
        elif direction is Direction.DOWN and steps_taken < 10:
            possible_movements.update({(row + 1, column, Direction.DOWN, steps_taken + 1): data[row + 1][column]})
    # left
    if column > 0 and direction is not direction.RIGHT:
        if direction is not Direction.LEFT and (steps_taken > 3 or steps_taken == 0):
            possible_movements.update({(row, column - 1, Direction.LEFT, 1): data[row][column - 1]})
        elif direction is Direction.LEFT and steps_taken < 10:
            possible_movements.update({(row, column - 1, Direction.LEFT, steps_taken + 1): data[row][column - 1]})
    return possible_movements


def reverse_path(previous: dict[MovementNode, MovementNode], node: MovementNode) -> list[MovementNode]:
    li = [node]
    n = node
    while previous.get(n, None) is not None:
        n = previous.get(n)
        li.append(n)
    return list(reversed(li))


def draw_path(data: Grid, movement: list[MovementNode]) -> Grid:
    newgrid = data.copy()
    for m in movement:
        row, column, direction, _ = m
        symbol = "."
        match direction:
            case Direction.UP:
                symbol = "^"
            case Direction.RIGHT:
                symbol = ">"
            case Direction.DOWN:
                symbol = "v"
            case Direction.LEFT:
                symbol = "<"
        newgrid[row][column] = symbol
    return newgrid


def dijkstra(data: Grid, start_position: MovementNode, destination: tuple[int, int], ultra: bool = False) -> int:
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
            if ultra:
                pm = calculate_possible_movements_ultra(data, current_position)
            else:
                pm = calculate_possible_movements(data, current_position)
            for possible_movement, distance in pm.items():
                alt = distances.get(current_position) + distance
                if alt < distances.get(possible_movement, sys.maxsize):
                    distances.update({possible_movement: alt})
                    previous.update({possible_movement: current_position})
                    q.put((alt, possible_movement))
    terminal_distances = [distances.get(n) for n in terminal_nodes]
    rev_path = reverse_path(previous, list(terminal_nodes)[0])
    grid_with_path = draw_path(data, rev_path)
    return min(terminal_distances)


def exercise_1(data: Grid) -> int:
    return dijkstra(data, (0, 0, Direction.RIGHT, 0), (len(data)-1, len(data[0])-1))


def exercise_2(data: Grid) -> int:
    return dijkstra(data, (0, 0, Direction.RIGHT, 0), (len(data)-1, len(data[0])-1), True)
