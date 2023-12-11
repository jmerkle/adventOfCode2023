import numpy as np


def read_file_as_array_and_filter_empty_lines(filename: str) -> np.ndarray:
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return np.array([list(x) for x in data.split("\n") if len(x) > 0])


def find_expanding_lines(data: np.ndarray) -> list[int]:
    expanding_lines = []
    for line in range(0, data.shape[0]):
        if all(c == "." for c in data[line, :]):
            expanding_lines.append(line)
    return expanding_lines


def find_expanding_columns(data: np.ndarray) -> list[int]:
    expanding_columns = []
    for column in range(0, data.shape[1]):
        if all(c == "." for c in data[:, column]):
            expanding_columns.append(column)
    return expanding_columns


def exercise_1(data: np.ndarray) -> int:
    expanding_line = find_expanding_lines(data)
    expanding_columns = find_expanding_columns(data)
    return 0
