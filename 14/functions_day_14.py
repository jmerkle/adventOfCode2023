import numpy as np
from functools import lru_cache, wraps


def read_file_as_list_of_lines_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


def as_matrix(data: list[str]) -> np.ndarray:
    return np.array(list(map(lambda line: list(line), data)))


def rotate_matrix_so_direction_points_right(matrix: np.ndarray, direction: str) -> np.ndarray:
    if direction == "n":
        return np.rot90(matrix, 3)
    if direction == "w":
        return np.rot90(matrix, 2)
    if direction == "s":
        return np.rot90(matrix, 1)
    return matrix


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


def calculate_load(matrix: np.ndarray, direction: str) -> int:
    rotated = rotate_matrix_so_direction_points_right(matrix, direction)
    locations_of_rocks = np.where(rotated == "O")
    return sum(locations_of_rocks[1]) + + len(locations_of_rocks[1])


def platform_to_tuple(matrix: np.ndarray) -> tuple[str, int, int]:
    return "".join(matrix.flatten().tolist()), matrix.shape[0], matrix.shape[1]


def tuple_to_platform(platform_tuple: tuple[str, int, int]):
    return np.array(list(platform_tuple[0])).reshape(platform_tuple[1], platform_tuple[2])


def np_cache(function):
    @lru_cache(maxsize=1024)
    def cached_wrapper(platform_tuple):
        array = tuple_to_platform(platform_tuple)
        return function(array)

    @wraps(function)
    def wrapper(array):
        return cached_wrapper(platform_to_tuple(array))

    # copy lru_cache attributes over too
    wrapper.cache_info = cached_wrapper.cache_info
    wrapper.cache_clear = cached_wrapper.cache_clear

    return wrapper


@np_cache
def run_cycle(matrix: np.ndarray) -> np.ndarray:
    tilt_platform(matrix, "n")
    tilt_platform(matrix, "w")
    tilt_platform(matrix, "s")
    tilt_platform(matrix, "e")
    return matrix


def exercise_1(data: list[str]) -> int:
    platform = as_matrix(data)
    tilt_platform(platform, "n")
    return calculate_load(platform, "n")


def exercise_2(data: list[str]) -> int:
    platform = as_matrix(data)
    for c in range(0, 1000000000):
        platform = run_cycle(platform.copy())
    return calculate_load(platform, "n")
