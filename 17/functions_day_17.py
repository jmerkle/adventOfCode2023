from enum import Enum
from typing import TypeAlias


class Direction(Enum):
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
    if row > 0:
        if direction is not Direction.UP:
            possible_movements.update({(row-1, column, Direction.UP, 1): data[row-1][column]})
        elif steps_taken < 3:
            possible_movements.update({(row-1, column, Direction.UP, steps_taken + 1): data[row-1][column]})
    # right
    if column < len(data[0])-1:
        if direction is not Direction.RIGHT:
            possible_movements.update({(row, column+1, Direction.RIGHT, 1): data[row][column+1]})
        elif steps_taken < 3:
            possible_movements.update({(row, column+1, Direction.RIGHT, steps_taken + 1): data[row][column+1]})
    # down
    if row < len(data)-1:
        if direction is not Direction.DOWN:
            possible_movements.update({(row+1, column, Direction.DOWN, 1): data[row+1][column]})
        elif steps_taken < 3:
            possible_movements.update({(row+1, column, Direction.DOWN, steps_taken + 1): data[row+1][column]})
    # left
    if column > 0:
        if direction is not Direction.LEFT:
            possible_movements.update({(row, column-1, Direction.LEFT, 1): data[row][column-1]})
        elif steps_taken < 3:
            possible_movements.update({(row, column-1, Direction.LEFT, steps_taken + 1): data[row][column-1]})
    return possible_movements



def exercise_1(data: Grid) -> int:
    return 0
