from enum import Enum
from heapq import merge
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
Edges: TypeAlias = dict[int, list[int]]
Edge: TypeAlias = tuple[int, list[int]]
Position: TypeAlias = tuple[int, int]


def parse_command(command_string: str) -> Command:
    d, n, h = command_string.split()
    return Direction(d), int(n)


def insert_edge(edge_dictionary: Edges, edge: Edge) -> Edges:
    row, columns = edge
    existing_columns = edge_dictionary.get(row, [])
    edge_dictionary.update({row: list(merge(existing_columns, columns))})
    return edge_dictionary


def draw_right(horizontal_edges: Edges, vertical_edges: Edges, position: Position, num_steps: int) -> tuple[Edges, Edges, Position]:
    row, column = position
    new_edge = (row, list(range(column, column + num_steps + 1)))
    horizontal_edges = insert_edge(horizontal_edges, new_edge)
    return horizontal_edges, vertical_edges, (row, column + num_steps)


def draw_left(horizontal_edges: Edges, vertical_edges: Edges, position: Position, num_steps: int) -> tuple[Edges, Edges, Position]:
    row, column = position
    new_edge = (row, list(reversed(range(column, column - num_steps - 1, -1))))
    horizontal_edges = insert_edge(horizontal_edges, new_edge)
    return horizontal_edges, vertical_edges, (row, column - num_steps)


def draw_down(horizontal_edges: Edges, vertical_edges: Edges, position: Position, num_steps: int) -> tuple[Edges, Edges, Position]:
    row, column = position
    new_edge = (column, list(range(row + 1, row + num_steps)))
    vertical_edges = insert_edge(vertical_edges, new_edge)
    return horizontal_edges, vertical_edges, (row + num_steps, column)


def draw_up(horizontal_edges: Edges, vertical_edges: Edges, position: Position, num_steps: int) -> tuple[Edges, Edges, Position]:
    row, column = position
    new_edge = (column, list(reversed(range(row - 1, row - num_steps, -1))))
    vertical_edges = insert_edge(vertical_edges, new_edge)
    return horizontal_edges, vertical_edges, (row - num_steps, column)


def draw(horizontal_edges: Edges, vertical_edges: Edges, position: Position, command: Command) -> tuple[Edges, Edges, Position]:
    direction, num_steps = command
    match direction:
        case Direction.RIGHT:
            return draw_right(horizontal_edges, vertical_edges, position, num_steps)
        case Direction.DOWN:
            return draw_down(horizontal_edges, vertical_edges, position, num_steps)
        case Direction.LEFT:
            return draw_left(horizontal_edges, vertical_edges, position, num_steps)
        case Direction.UP:
            return draw_up(horizontal_edges, vertical_edges, position, num_steps)


def draw_commands(commands: list[Command]) -> tuple[Edges, Edges]:
    horizontal_edges = {}
    vertical_edges = {}
    position = (0, 0)
    for command in commands:
        horizontal_edges, vertical_edges, position = draw(horizontal_edges, vertical_edges, position, command)
    return horizontal_edges, vertical_edges


def draw_fill_and_calc_size(commands: list[Command]) -> int:
    horizontal_edges, vertical_edges = draw_commands(commands)
    return 0


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
