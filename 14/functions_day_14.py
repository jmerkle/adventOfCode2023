import numpy as np


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


def run_cycle(matrix: np.ndarray) -> np.ndarray:
    tilt_platform(matrix, "n")
    tilt_platform(matrix, "w")
    tilt_platform(matrix, "s")
    tilt_platform(matrix, "e")
    return matrix


def merge_dictionaries(dict1, dict2):
    return {key: dict1.get(key, []) + dict2.get(key, []) for key in set(dict1.keys()) | set(dict2.keys())}


def platform_as_string(matrix: np.ndarray) -> str:
    return "".join(matrix.flatten().tolist())


def exercise_1(data: list[str]) -> int:
    platform = as_matrix(data)
    tilt_platform(platform, "n")
    return calculate_load(platform, "n")


def exercise_2(data: list[str]) -> int:
    max_cycles = 1000000000
    platform = as_matrix(data)
    platform_string = platform_as_string(platform)
    cycle_tracker = {}
    cycle_detected = False
    c = -1
    while not cycle_detected and c < max_cycles:
        c += 1
        run_cycle(platform)
        platform_string = platform_as_string(platform)
        cycle_tracker = merge_dictionaries(cycle_tracker, {platform_as_string(platform): [c]})
        if len(cycle_tracker.get(platform_string)) > 1:
            cycle_detected = True
    cycle = cycle_tracker.get(platform_string)
    remaining_cycles = (max_cycles - max(cycle)) % (max(cycle) - min(cycle))
    print("cycle detected at ", cycle, ", ", remaining_cycles, " cycles remaining.")
    for i in range(0, remaining_cycles - 1):
        run_cycle(platform)
    return calculate_load(platform, "n")
