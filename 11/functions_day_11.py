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


def find_distance(galaxy_a: tuple[int, int], galaxy_b: tuple[int, int], expanding_lines: list[int], expanding_columns: list[int]):
    line_coords_ordered = sorted([galaxy_a[0], galaxy_b[0]])
    column_coords_ordered = sorted([galaxy_a[1], galaxy_b[1]])
    distance = line_coords_ordered[1] - line_coords_ordered[0] + column_coords_ordered[1] - column_coords_ordered[0]
    distance += sum([line_coords_ordered[0] < line < line_coords_ordered[1] for line in expanding_lines])*(1000000-1)
    distance += sum([column_coords_ordered[0] < column < column_coords_ordered[1] for column in expanding_columns])*(1000000-1)
    return distance


def find_all_distances_between_galaxies(galaxy_coords: tuple[list[int], list[int]], expanding_lines: list[int], expanding_columns: list[int]) -> list[int]:
    distances = []
    for galaxy_a_idx in range(0, len(galaxy_coords[0])):
        galaxy_a = (galaxy_coords[0][galaxy_a_idx], galaxy_coords[1][galaxy_a_idx])
        for galaxy_b_idx in range(galaxy_a_idx + 1, len(galaxy_coords[0])):
            galaxy_b = (galaxy_coords[0][galaxy_b_idx], galaxy_coords[1][galaxy_b_idx])
            distances.append(find_distance(galaxy_a, galaxy_b, expanding_lines, expanding_columns))
    return distances


def exercise_1(data: np.ndarray) -> int:
    expanding_lines = find_expanding_lines(data)
    expanding_columns = find_expanding_columns(data)
    galaxy_coords = np.where(data == '#')
    distances = find_all_distances_between_galaxies(galaxy_coords, expanding_lines, expanding_columns)
    return sum(distances)
