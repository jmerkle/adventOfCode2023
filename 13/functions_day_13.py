import math

import numpy as np


def read_file_as_list_of_sections(filename: str) -> list[list[str]]:
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x.strip().split("\n") for x in data.split("\n\n") if len(x) > 0]


def split_and_compare(l: list[int], split_at: int) -> bool:
    if split_at == 0:
        return False
    left = list(reversed(l[:split_at]))
    right = l[split_at:]
    if len(left) > len(right):
        return left[: len(right)] == right
    else:
        return left == right[: len(left)]


def find_middle(l: list[int]) -> int:
    middle = 0
    while not split_and_compare(l, middle):
        middle += 1
        if middle >= len(l):
            return -1
    return middle


def find_multiple_middles(l: list[int]) -> list[int]:
    middles = [middle for middle in range(0, len(l)) if split_and_compare(l, middle)]
    return middles


def process_pattern(pattern: list[str]) -> int:
    return process_matrix(np.array(list(map(lambda line: list(line), pattern))))


def process_matrix(matrix: np.ndarray, ignore_value: int = -1) -> int:
    _, order_rows = np.unique(matrix, axis=0, return_inverse=True)
    horizontal = find_multiple_middles(list(order_rows))
    _, order_columns = np.unique(matrix, axis=1, return_inverse=True)
    vertical = find_multiple_middles(list(order_columns))
    all_values = [v*100 for v in horizontal] + vertical
    if len(all_values) > 1 and all_values[0] == ignore_value:
        return all_values[1]
    if len(all_values) > 0:
        return all_values[0]
    return -1


def smudge_character(matrix: np.ndarray, character_index: int) -> np.ndarray:
    row, column = math.floor(character_index/matrix.shape[1]), character_index % matrix.shape[1]
    if matrix[row, column] == ".":
        matrix[row, column] = "#"
    else:
        matrix[row, column] = "."
    return matrix


def process_smudged_pattern(pattern: list[str]) -> int:
    unsmudged_value = process_pattern(pattern)
    matrix = np.array(list(map(lambda line: list(line), pattern)))
    smudged_character_index = 0
    smudged_value = -1
    while smudged_value in [-1, unsmudged_value]:
        smudged_value = process_matrix(smudge_character(matrix.copy(), smudged_character_index), unsmudged_value)
        smudged_character_index += 1
    return smudged_value


def exercise_1(data: list[list[str]]) -> int:
    return sum(list(map(process_pattern, data)))


def exercise_2(data: list[list[str]]) -> int:
    return sum(list(map(process_smudged_pattern, data)))
