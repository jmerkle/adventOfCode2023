import numpy as np

def read_file_as_list_of_lines_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


def as_matrix(data: list[str]) -> np.ndarray:
    return np.array(list(map(lambda line: list(line), data)))


def rotate_matrix_so_direction_points_right(matrix: np.ndarray, direction: str) -> np.ndarray:
    return np.rot90(matrix, 3)


def flatten_list(xss):
    return [x for xs in xss for x in xs]


def tilt_line(line: np.ndarray) -> np.ndarray:
    # TODO: this code hurts
    split_line = np.split(line.flatten(), np.where(line.flatten() == "#")[0])
    sorted_splits = [sorted(split) for split in split_line]
    return np.array(flatten_list(sorted_splits))


def tilt_platform(matrix: np.ndarray, direction: str) -> np.ndarray:
    rotated = rotate_matrix_so_direction_points_right(matrix, direction)
    for line in range(0, rotated.shape[0]):
        rotated[line] = tilt_line(rotated[line])
    return matrix

def exercise_1(data: list[str]) -> int:
    platform = as_matrix(data)
    tilted = tilt_platform(platform, "n")
    return 0

