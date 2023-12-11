from functions_day_11 import *
import numpy as np

data_small = read_file_as_array_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_array_and_filter_empty_lines('input.txt')


def test_find_expanding_lines():
    assert find_expanding_lines(data_small) == [3, 7]


def test_find_expanding_columns():
    assert find_expanding_columns(data_small) == [2, 5, 8]


def test_exercise_1():
    assert exercise_1(data_small) == 374
