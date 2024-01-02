from enum import Enum
from typing import TypeAlias
import queue
import numpy as np


def read_file_as_list_of_lines_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


class Direction(Enum):
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"
    UP = "U"


Command: TypeAlias = tuple[Direction, int]
Grid: TypeAlias = np.ndarray
Position: TypeAlias = tuple[int, int]


def parse_command(command_string: str) -> Command:
    d, n, h = command_string.split()
    return Direction(d), int(n)


def draw_right(grid: Grid, position: Position, num_steps: int) -> tuple[Grid, Position]:
    row, column = position
    resize_by = column + num_steps - grid.shape[1] + 1
    if resize_by > 0:
        grid = resize_right(grid, resize_by)
    grid[row, column:column + num_steps + 1] = np.ones([1, num_steps + 1])
    return grid, (row, column + num_steps)


def draw_left(grid: Grid, position: Position, num_steps: int) -> tuple[Grid, Position]:
    row, column = position
    resize_by = num_steps - column
    if resize_by > 0:
        grid = resize_left(grid, resize_by)
        column = column + resize_by
    grid[row, column - num_steps:column + 1] = np.ones([1, num_steps + 1])
    return grid, (row, column - num_steps)


def draw_down(grid: Grid, position: Position, num_steps: int) -> tuple[Grid, Position]:
    row, column = position
    resize_by = row + num_steps - grid.shape[0] + 1
    if resize_by > 0:
        grid = resize_down(grid, resize_by)
    grid[row:row + num_steps + 1, column] = np.ones([num_steps + 1])
    return grid, (row + num_steps, column)


def draw_up(grid: Grid, position: Position, num_steps: int) -> tuple[Grid, Position]:
    row, column = position
    resize_by = num_steps - row
    if resize_by > 0:
        grid = resize_up(grid, resize_by)
        row = row + resize_by
    grid[row - num_steps:row + 1, column] = np.ones([num_steps + 1])
    return grid, (row - num_steps, column)


def draw(grid: Grid, position: Position, command: Command) -> tuple[Grid, Position]:
    direction, num_steps = command
    match direction:
        case Direction.RIGHT:
            return draw_right(grid, position, num_steps)
        case Direction.DOWN:
            return draw_down(grid, position, num_steps)
        case Direction.LEFT:
            return draw_left(grid, position, num_steps)
        case Direction.UP:
            return draw_up(grid, position, num_steps)


def resize_right(grid: Grid, n: int) -> Grid:
    grid = np.c_[grid, np.zeros([grid.shape[0], n])]
    return grid


def resize_left(grid: Grid, n: int) -> Grid:
    grid = np.c_[np.zeros([grid.shape[0], n]), grid]
    return grid


def resize_down(grid: Grid, n: int) -> Grid:
    num_columns = grid.shape[1]
    grid = np.r_[grid, np.zeros([n, num_columns])]
    return grid


def resize_up(grid: Grid, n: int) -> Grid:
    num_columns = grid.shape[1]
    grid = np.r_[np.zeros([n, num_columns]), grid]
    return grid


def matrix_to_string(data: Grid) -> str:
    return np.array2string(data)


def find_inner_point(grid: Grid) -> Position:
    for row in range(grid.shape[0]):
        if (grid[row, 0:2].tolist() == np.array([1, 0])).all():
            return row, 1
        for column in range(grid.shape[1] - 2):
            if (grid[row, column:column + 3] == [0, 1, 0]).all():
                return row, column + 2


def fill_shape(grid: Grid, inner_point: Position) -> Grid:
    point_queue = queue.Queue()
    point_queue.put(inner_point)
    while point_queue.qsize() > 0:
        row, column = point_queue.get()
        if grid[row, column] == 0:
            grid[row, column] = 1
            point_queue.put((row - 1, column))
            point_queue.put((row, column + 1))
            point_queue.put((row + 1, column))
            point_queue.put((row, column - 1))
    return grid


def draw_commands(commands: list[Command]) -> Grid:
    grid = np.array([[0]])
    position = (0, 0)
    for command in commands:
        grid, position = draw(grid, position, command)
    return grid


def draw_fill_and_calc_size(commands: list[Command]) -> int:
    grid = draw_commands(commands)
    inner_point = find_inner_point(grid)
    filled_grid = fill_shape(grid, inner_point)
    return np.count_nonzero(filled_grid == 1)


def exercise_1(data: list[str]) -> int:
    commands = list(map(parse_command, data))
    return draw_fill_and_calc_size(commands)


def hex_to_command(input_string: str) -> Command:
    _, hex_string = input_string.split("(")
    distance = int(hex_string[1:6], base=16)
    direction = int(hex_string[6], base=16)
    return list(Direction)[direction], distance


def exercise_2(data: list[str]) -> int:
    commands = list(map(hex_to_command, data))
    return draw_fill_and_calc_size(commands)
