from functions_day_10 import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
data_small_more_complex = read_file_as_list_of_lines_and_filter_empty_lines('input_small_more_complex.txt')
data_full = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')


def test_exercise_1():
    assert exercise_1(data_small) == 4
    assert exercise_1(data_small_more_complex) == 8


def test_exercise_1_full():
    print(exercise_1(data_full))
