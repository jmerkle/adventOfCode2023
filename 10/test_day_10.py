from functions_day_10 import *

data_small = read_file_as_list_of_list_of_chars_and_filter_empty_lines('input_small.txt')
data_small_more_complex = read_file_as_list_of_list_of_chars_and_filter_empty_lines('input_small_more_complex.txt')
data_small_exercise_2 = read_file_as_list_of_list_of_chars_and_filter_empty_lines('input_exercise_2_test.txt')
data_full = read_file_as_list_of_list_of_chars_and_filter_empty_lines('input.txt')


def test_exercise_1():
    assert exercise_1(data_small, 1, 1, "R") == 4
    assert exercise_1(data_small, 1, 1, "D") == 4
    assert exercise_1(data_small_more_complex, 2, 0, "D") == 8
    assert exercise_1(data_small_more_complex, 2, 0, "R") == 8


def test_exercise_1_full():
    assert (exercise_1(data_full, 62, 61, "D")) == 6815
    assert (exercise_1(data_full, 62, 61, "L")) == 6815


def test_exercise_2():
    assert exercise_2(data_small_exercise_2, 1, 1, "R", "F", "U") == 4


def test_exercise_2_full():
    assert exercise_2(data_full, 62, 61, "D", "7", "R") == 269

