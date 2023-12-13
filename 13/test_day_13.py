from functions_day_13 import *

data_small = read_file_as_list_of_sections('input_small.txt')
data_full = read_file_as_list_of_sections('input.txt')


def test_exercise_1():
    assert exercise_1(data_small) == 405
