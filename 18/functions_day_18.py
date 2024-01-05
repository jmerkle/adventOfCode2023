from enum import Enum
from heapq import merge
from itertools import groupby, count
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


def calculate_boundary_size(horizontal_edges: Edges, vertical_edges: Edges) -> int:
    return sum([len(v) for v in horizontal_edges.values()]) + sum([len(v) for v in vertical_edges.values()])


def sorted_list_of_numbers_as_ranges(numbers: list[int]) -> list[tuple[int, int]]:
    if numbers is None:
        return []
    return [(li[0], li[-1]) for li in [list(g) for k, g in groupby(numbers, key=lambda i, j=count(): i-next(j))]]


def is_boundary_edge(row: int, column_range: tuple[int, int], vertical_edges: Edges) -> bool:
    if row-1 in vertical_edges.get(column_range[0]) and row-1 in vertical_edges.get(column_range[1]):
        return True
    if row+1 in vertical_edges.get(column_range[0]) and row+1 in vertical_edges.get(column_range[1]):
        return True
    return False


def remove_boundary_edges(row: int, horizontal_edges_in_row: list[tuple[int, int]], vertical_edges_in_row: list[int], vertical_edges: Edges) -> tuple[list[tuple[int, int]], int]:
    boundary_edge_size = 0
    while len(horizontal_edges_in_row) > 0 and is_boundary_edge(row, horizontal_edges_in_row[0], vertical_edges):
        left, right = horizontal_edges_in_row[0]
        if len(vertical_edges_in_row) > 0 and left > vertical_edges_in_row[0]:
            return horizontal_edges_in_row, boundary_edge_size
        boundary_edge_size += right - left + 1
        horizontal_edges_in_row = horizontal_edges_in_row[1:]
    return horizontal_edges_in_row, boundary_edge_size


def calculate_inner_size_row(row: int, horizontal_edges: Edges, vertical_edges: Edges, vertical_edges_per_row: Edges) -> int:
    print(f"processing row {row}")
    horizontal_edges_in_row = sorted_list_of_numbers_as_ranges(horizontal_edges.get(row))
    # vertical_edges_in_row_tmp = [c for c in sorted(vertical_edges.keys()) if row in vertical_edges.get(c)]
    vertical_edges_in_row = vertical_edges_per_row.get(row, [])
    # vertical_edges_in_row = list(set(vertical_edges_per_row.get(row, [])))
    size = 0
    horizontal_edges_in_row, _ = remove_boundary_edges(row, horizontal_edges_in_row, vertical_edges_in_row, vertical_edges)
    while len(horizontal_edges_in_row) > 0 or len(vertical_edges_in_row) > 0:
        if len(horizontal_edges_in_row) == 0:
            size = size + vertical_edges_in_row[1] - vertical_edges_in_row[0] - 1
            vertical_edges_in_row = vertical_edges_in_row[2:]
        elif len(vertical_edges_in_row) == 0:
            _, left_boundary = horizontal_edges_in_row[0]
            horizontal_edges_in_row = horizontal_edges_in_row[1:]
            horizontal_edges_in_row, boundary_edge_size = remove_boundary_edges(row, horizontal_edges_in_row, vertical_edges_in_row, vertical_edges)
            right_boundary, _ = horizontal_edges_in_row[0]
            size += right_boundary - left_boundary - boundary_edge_size - 1
            horizontal_edges_in_row = horizontal_edges_in_row[1:]
        else:
            _, left_boundary_horizontal = horizontal_edges_in_row[0]
            left_boundary_vertical = vertical_edges_in_row[0]
            if left_boundary_horizontal < left_boundary_vertical:
                left_boundary = left_boundary_horizontal
                horizontal_edges_in_row = horizontal_edges_in_row[1:]
            else:
                left_boundary = left_boundary_vertical
                vertical_edges_in_row = vertical_edges_in_row[1:]
            horizontal_edges_in_row, boundary_edge_size = remove_boundary_edges(row, horizontal_edges_in_row, vertical_edges_in_row, vertical_edges)
            if len(horizontal_edges_in_row) == 0:
                right_boundary = vertical_edges_in_row[0]
                vertical_edges_in_row = vertical_edges_in_row[1:]
            elif len(vertical_edges_in_row) == 0:
                right_boundary, _ = horizontal_edges_in_row[0]
                horizontal_edges_in_row = horizontal_edges_in_row[1:]
            else:
                right_boundary_horizontal, _ = horizontal_edges_in_row[0]
                right_boundary_vertical = vertical_edges_in_row[0]
                if right_boundary_horizontal < right_boundary_vertical:
                    right_boundary = right_boundary_horizontal
                    horizontal_edges_in_row = horizontal_edges_in_row[1:]
                else:
                    right_boundary = right_boundary_vertical
                    vertical_edges_in_row = vertical_edges_in_row[1:]
            size += right_boundary - left_boundary - boundary_edge_size - 1
            horizontal_edges_in_row, _ = remove_boundary_edges(row, horizontal_edges_in_row, vertical_edges_in_row, vertical_edges)
    return size


def calculate_inner_size(horizontal_edges: Edges, vertical_edges: Edges, vertical_edges_per_row: Edges) -> int:
    return sum([calculate_inner_size_row(r, horizontal_edges, vertical_edges, vertical_edges_per_row) for r in range(min(horizontal_edges.keys()) + 1, max(horizontal_edges.keys()))])


def generate_vertical_edges_per_row(vertical_edges: Edges) -> Edges:
    vertical_edges_per_row = {}
    for column in sorted(vertical_edges.keys()):
        print(f"column {column}")
        edge = vertical_edges.get(column)
        for row in edge:
            vertical_edges_per_row = insert_edge(vertical_edges_per_row, (row, [column]))
    return vertical_edges_per_row


def draw_fill_and_calc_size(commands: list[Command]) -> int:
    horizontal_edges, vertical_edges = draw_commands(commands)
    vertical_edges_per_row = generate_vertical_edges_per_row(vertical_edges)
    boundary_size = calculate_boundary_size(horizontal_edges, vertical_edges)
    inner_size = calculate_inner_size(horizontal_edges, vertical_edges, vertical_edges_per_row)
    return boundary_size + inner_size


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
