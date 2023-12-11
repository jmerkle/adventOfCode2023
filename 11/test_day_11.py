from functions_day_11 import *

data_small = read_file_as_array_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_array_and_filter_empty_lines('input.txt')


def test_find_expanding_lines():
    assert find_expanding_lines(data_small) == [3, 7]


def test_find_expanding_columns():
    assert find_expanding_columns(data_small) == [2, 5, 8]


def test_find_distance():
    assert find_distance((0, 3), (1, 7), [3, 7], [2, 5, 8]) == 6
    assert find_distance((0, 3), (2, 0), [3, 7], [2, 5, 8]) == 6
    assert find_distance((1, 7), (2, 0), [3, 7], [2, 5, 8]) == 10


def test_find_all_distances_between_galaxies():
    assert find_all_distances_between_galaxies(([0, 1, 2], [3, 7, 0]), [], [2, 5, 8]) == [6, 6, 10]


def test_exercise_1():
    assert exercise_1(data_small) == 374


def test_exercise_1_all_data():
    assert exercise_1(data_full) == 9565386
