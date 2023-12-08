from collections import Counter


def read_file_as_instructions_and_maps(filename: str) -> tuple[str, list[str]]:
    f = open(filename, 'r')
    data = f.read()
    f.close()
    lines = data.split("\n")
    return lines[0], [x for x in lines[1:] if len(x) > 0]


def exercise_1(data: tuple[str, list[str]]) -> int:
    return 0
