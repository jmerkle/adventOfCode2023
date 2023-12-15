from typing import Optional


def read_file_and_split_on_comma(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    lines = [x for x in data.split("\n") if len(x) > 0]
    return lines[0].split(",")


def hash_function(input_string: str) -> int:
    current_value = 0
    for c in list(input_string):
        current_value = (current_value + ord(c))*17 % 256
    return current_value


def exercise_1(data: list[str]) -> int:
    return sum(list(map(hash_function, data)))


def box_and_operation(step_input: str) -> tuple[int, Optional[int]]:
    if step_input[-1] == "-":
        return hash_function(step_input[:-1]), None
    label, focal_length = step_input.split("=")
    return hash_function(label), int(focal_length)
