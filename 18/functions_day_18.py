from enum import Enum
from typing import TypeAlias


def read_file_as_list_of_lines_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


class Direction(Enum):
    UP = "U"
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"


Command: TypeAlias = tuple[Direction, int, hex]
Grid: TypeAlias = list[list[str]]
Position: TypeAlias = tuple[int, int]


def parse_command(command_string: str) -> Command:
    d, n, h = command_string.split()
    return Direction(d), int(n), int("0x" + h[2:-1], base=16)


def draw_right(grid: Grid, position: Position, num_steps: int) -> tuple[Grid, Position]:
    row, column = position
    resize_by = column + num_steps - len(grid[0]) + 1
    if resize_by > 0:
        resize_right(grid, resize_by)
    grid[row][column:column+num_steps+1] = ["#" for _ in range(num_steps+1)]
    return grid, (row, column + num_steps)


def draw_down(grid: Grid, position: Position, num_steps: int) -> tuple[Grid, Position]:
    row, column = position
    resize_by = row + num_steps - len(grid) + 1
    if resize_by > 0:
        resize_down(grid, resize_by)
    for r in range(row, row+num_steps + 1):
        grid[r][column] = "#"
    return grid, (row + num_steps, column)


def draw(grid: Grid, position: Position, command: Command) -> tuple[Grid, Position]:
    direction, num_steps, _ = command
    match direction:
        case Direction.RIGHT:
            return draw_right(grid, position, num_steps)
        case Direction.DOWN:
            return draw_down(grid, position, num_steps)
    return 0


def resize_right(grid: Grid, n: int) -> Grid:
    [row.extend(["." for _ in range(n)]) for row in grid]
    return grid


def resize_down(grid: Grid, n: int) -> Grid:
    num_columns = len(grid[0])
    new_rows = [["." for _ in range(num_columns)] for _ in range(n)]
    grid = grid.extend(new_rows)
    return grid


def exercise_1(data: list[str]) -> int:
    return 0
