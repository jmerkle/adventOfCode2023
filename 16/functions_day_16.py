from typing import TypeAlias

Grid: TypeAlias = list[list[str]]


def read_file_as_list_of_list_and_filter_empty_lines(filename: str) -> Grid:
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [list(x) for x in data.split("\n") if len(x) > 0]


def exercise_1(data: Grid) -> int:
    return 0

