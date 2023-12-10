import math


def read_file_as_list_of_lines_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


def calc_position(position_line: int, position_column: int, direction: str) -> tuple[int, int]:
    new_line = position_line
    new_column = position_column
    if direction == "U":
        new_line -= 1
    if direction == "D":
        new_line += 1
    if direction == "L":
        new_column -= 1
    if direction == "R":
        new_column += 1
    return new_line, new_column


def calc_direction(direction: str, pipe_shape: str) -> str:
    if pipe_shape == "|" or pipe_shape == "-":
        return direction
    if pipe_shape == "L" and direction == "D":
        return "R"
    if pipe_shape == "L" and direction == "L":
        return "U"
    if pipe_shape == "J" and direction == "D":
        return "L"
    if pipe_shape == "J" and direction == "R":
        return "U"
    if pipe_shape == "7" and direction == "U":
        return "L"
    if pipe_shape == "7" and direction == "R":
        return "D"
    if pipe_shape == "F" and direction == "U":
        return "R"
    if pipe_shape == "F" and direction == "L":
        return "D"
    if pipe_shape == "S":
        return "S"
    raise Exception("cannot go to ", pipe_shape, " with ", direction)


def take_step(data: list[str], position_line: int, position_column: int, direction: str) -> tuple[int, int, str]:
    new_line, new_column = calc_position(position_line, position_column, direction)
    new_tile = data[new_line][new_column]
    new_direction = calc_direction(direction, new_tile)
    return new_line, new_column, new_direction


def exercise_1(data: list[str], start_line: int, start_column: int, start_direction: str) -> int:
    steps_taken = 0
    position_line = start_line
    position_column = start_column
    direction = start_direction
    while direction != "S":
        position_line, position_column, direction = take_step(data, position_line, position_column, direction)
        steps_taken += 1
    return math.ceil(steps_taken/2)
