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


def parse_command(command_string: str) -> Command:
    d, n, h = command_string.split()
    return Direction(d), int(n), int("0x" + h[2:-1], base=16)


def exercise_1(data: list[str]) -> int:
    return 0
