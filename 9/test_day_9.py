from functions_day_9 import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')


def test_derive_line():
    assert derive_line([0, 3, 6, 9, 12, 15]) == [3, 3, 3, 3, 3]
    assert derive_line([3, 3, 3, 3, 3]) == [0, 0, 0, 0]
    assert derive_line([0, 0, 0, 0]) == [0, 0, 0]


def test_derive_all_line():
    assert derive_all_line([0, 3, 6, 9, 12, 15]) == [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]]


def test_extrapolate():
    assert (extrapolate([[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]])
            == [[0, 3, 6, 9, 12, 15, 18], [3, 3, 3, 3, 3, 3], [0, 0, 0, 0, 0]])


def test_exercise_1():
    assert exercise_1(data_small) == 114


def test_exercise_1_full():
    print(exercise_1(data_full))

