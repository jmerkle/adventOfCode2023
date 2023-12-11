import math


def read_file_as_list_of_list_of_chars_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [list(x) for x in data.split("\n") if len(x) > 0]


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


def mark_areas(areas: list[list[str]], position_line: int, position_column: int, direction: str, pipe_shape: str) -> list[list[str]]:
    if pipe_shape == "|" and direction == "D":
        areas[position_line][position_column-1] = "1"
        areas[position_line][position_column+1] = "0"
    if pipe_shape == "|" and direction == "U":
        areas[position_line][position_column-1] = "0"
        areas[position_line][position_column+1] = "1"
    if pipe_shape == "-" and direction == "R":
        areas[position_line-1][position_column] = "0"
        areas[position_line+1][position_column] = "1"
    if pipe_shape == "-" and direction == "L":
        areas[position_line-1][position_column] = "1"
        areas[position_line+1][position_column] = "0"
    if pipe_shape == "L" and direction == "D":
        areas[position_line+1][position_column] = "1"
        areas[position_line][position_column-1] = "1"
    if pipe_shape == "L" and direction == "L":
        areas[position_line+1][position_column] = "0"
        areas[position_line][position_column-1] = "0"
    if pipe_shape == "J" and direction == "D":
        areas[position_line+1][position_column] = "0"
        areas[position_line][position_column+1] = "0"
    if pipe_shape == "J" and direction == "R":
        areas[position_line+1][position_column] = "1"
        areas[position_line][position_column+1] = "1"
    if pipe_shape == "7" and direction == "U":
        areas[position_line-1][position_column] = "1"
        areas[position_line][position_column+1] = "1"
    if pipe_shape == "7" and direction == "R":
        areas[position_line-1][position_column] = "0"
        areas[position_line][position_column+1] = "0"
    if pipe_shape == "F" and direction == "U":
        areas[position_line-1][position_column] = "0"
        areas[position_line][position_column-1] = "0"
    if pipe_shape == "F" and direction == "L":
        areas[position_line-1][position_column] = "1"
        areas[position_line][position_column-1] = "1"
    return areas


def take_step(data: list[list[str]], areas: list[list[str]], position_line: int, position_column: int, direction: str) -> tuple[list[list[str]], int, int, str]:
    new_line, new_column = calc_position(position_line, position_column, direction)
    new_tile_pipe_shape = data[new_line][new_column]
    new_direction = calc_direction(direction, new_tile_pipe_shape)
    if len(areas) > 0:
        areas = mark_areas(areas, new_line, new_column, direction, new_tile_pipe_shape)
    return areas, new_line, new_column, new_direction


def exercise_1(data: list[list[str]], start_line: int, start_column: int, start_direction: str) -> int:
    steps_taken = 0
    position_line = start_line
    position_column = start_column
    direction = start_direction
    while direction != "S":
        _, position_line, position_column, direction = take_step(data, [[]], position_line, position_column, direction)
        steps_taken += 1
    return math.ceil(steps_taken/2)


def matrix_to_string(data: list[list[str]]) -> str:
    return "\n".join(["".join(line) for line in data])


def fill_with_dots(output: str) -> str:
    chars_to_replace = ["|", "-", "L", "J", "7", "F"]
    for c in chars_to_replace:
        output = output.replace(c, ".")
    return output


def initialise_exercise_2(data: list[list[str]], start_line: int, start_column: int, start_direction: str, start_pipe_shape: str, start_incoming_direction: str):
    areas = [["."]*len(data[0]) for i in range(len(data))]
    areas = mark_areas(areas, start_line, start_column, start_incoming_direction, start_pipe_shape)
    position_line = start_line
    position_column = start_column
    direction = start_direction
    return areas, position_line, position_column, direction


def post_process_exercise_2(data: list[list[str]], areas: list[list[str]]) -> int:
    visited_tiles = fill_with_dots(matrix_to_string(data))
    areas_as_string = matrix_to_string(areas)
    merged_maps = ""
    for i in range(len(visited_tiles)):
        if visited_tiles[i] == "*":
            merged_maps += "*"
        else:
            merged_maps += areas_as_string[i]
    while merged_maps.find("1.") > 0:
        merged_maps = merged_maps.replace("1.", "11")
    return sum([c == "1" for c in merged_maps])


def exercise_2(data: list[list[str]], start_line: int, start_column: int, start_direction: str, start_pipe_shape: str, start_incoming_direction: str)-> int:
    areas, position_line, position_column, direction = initialise_exercise_2(data, start_line, start_column, start_direction, start_pipe_shape, start_incoming_direction)
    while direction != "S":
        areas, position_line, position_column, direction = take_step(data, areas, position_line, position_column, direction)
        data[position_line][position_column] = "*"
    return post_process_exercise_2(data, areas)
