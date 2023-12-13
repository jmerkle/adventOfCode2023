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


def process_pattern(pattern: list[str]) -> int:
    matrix = np.array(list(map(lambda line: list(line), pattern)))
    _, order_rows = np.unique(matrix, axis=0, return_inverse=True)
    horizontal = find_middle(list(order_rows))
    if horizontal > 0:
        return horizontal*100
    _, order_columns = np.unique(matrix, axis=1, return_inverse=True)
    return find_middle(list(order_columns))


def exercise_1(data: list[list[str]]) -> int:
    return sum(list(map(process_pattern, data)))
