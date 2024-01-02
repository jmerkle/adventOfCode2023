from enum import Enum
from typing import TypeAlias
import queue


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
Grid: TypeAlias = list[list[str]]
Position: TypeAlias = tuple[int, int]


def parse_command(command_string: str) -> Command:
    d, n, h = command_string.split()
    return Direction(d), int(n)


def draw_right(grid: Grid, position: Position, num_steps: int) -> tuple[Grid, Position]:
    row, column = position
    resize_by = column + num_steps - len(grid[0]) + 1
    if resize_by > 0:
        grid = resize_right(grid, resize_by)
    grid[row][column:column+num_steps+1] = ["#" for _ in range(num_steps+1)]
    return grid, (row, column + num_steps)


def draw_left(grid: Grid, position: Position, num_steps: int) -> tuple[Grid, Position]:
    row, column = position
    resize_by = num_steps - column
    if resize_by > 0:
        grid = resize_left(grid, resize_by)
        column = column + resize_by
    grid[row][column-num_steps:column+1] = ["#" for _ in range(num_steps+1)]
    return grid, (row, column - num_steps)


def draw_down(grid: Grid, position: Position, num_steps: int) -> tuple[Grid, Position]:
    row, column = position
    resize_by = row + num_steps - len(grid) + 1
    if resize_by > 0:
        grid = resize_down(grid, resize_by)
    for r in range(row, row+num_steps + 1):
        grid[r][column] = "#"
    return grid, (row + num_steps, column)


def draw_up(grid: Grid, position: Position, num_steps: int) -> tuple[Grid, Position]:
    row, column = position
    resize_by = num_steps - row
    if resize_by > 0:
        grid = resize_up(grid, resize_by)
        row = row + resize_by
    for r in range(row-num_steps, row + 1):
        grid[r][column] = "#"
    return grid, (row - num_steps, column)


def draw(grid: Grid, position: Position, command: Command) -> tuple[Grid, Position]:
    direction, num_steps, _ = command
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
    [row.extend(["." for _ in range(n)]) for row in grid]
    return grid


def resize_left(grid: Grid, n: int) -> Grid:
    for r in range(len(grid)):
        grid[r] = ["." for _ in range(n)] + grid[r]
    return grid


def resize_down(grid: Grid, n: int) -> Grid:
    num_columns = len(grid[0])
    new_rows = [["." for _ in range(num_columns)] for _ in range(n)]
    grid.extend(new_rows)
    return grid


def resize_up(grid: Grid, n: int) -> Grid:
    num_columns = len(grid[0])
    new_rows = [["." for _ in range(num_columns)] for _ in range(n)]
    grid = new_rows + grid
    return grid


def matrix_to_string(data: list[list[str]]) -> str:
    return "\n".join(["".join(line) for line in data])


def find_inner_point(grid: Grid) -> Position:
    for row in range(len(grid)):
        if grid[row][0:2] == ["#", "."]:
            return row, 1
        for column in range(len(grid[0])-2):
            if grid[row][column:column+3] == [".", "#", "."]:
                return row, column + 2


def fill_shape(grid: Grid, inner_point: Position) -> Grid:
    point_queue = queue.Queue()
    point_queue.put(inner_point)
    while point_queue.qsize() > 0:
        row, column = point_queue.get()
        if grid[row][column] == ".":
            grid[row][column] = "#"
            point_queue.put((row - 1, column))
            point_queue.put((row, column + 1))
            point_queue.put((row + 1, column))
            point_queue.put((row, column - 1))
    return grid


def exercise_1(data: list[str]) -> int:
    grid = [["."]]
    position = (0, 0)
    for command_string in data:
        command = parse_command(command_string)
        grid, position = draw(grid, position, command)
        grid_as_string = matrix_to_string(grid)
        print(grid_as_string)
    inner_point = find_inner_point(grid)
    filled_grid = fill_shape(grid, inner_point)
    filled_grid_as_string = matrix_to_string(filled_grid)
    return filled_grid_as_string.count("#")


def hex_to_command(hex_string: str) -> Command:
    distance = int(hex_string[1:6], base=16)
    direction = int(hex_string[6], base=16)
    return list(Direction)[direction], distance

