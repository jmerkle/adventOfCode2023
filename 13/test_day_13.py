from functions_day_13 import *

data_small = read_file_as_list_of_sections('input_small.txt')
data_full = read_file_as_list_of_sections('input.txt')


def test_split_and_compare():
    assert not split_and_compare([1, 1, 2], 0)
    assert split_and_compare([1, 1, 2], 1)


def test_find_middle():
    assert find_middle([1, 1]) == 1
    assert find_middle([1, 2]) == -1
    assert find_middle([1, 1, 2]) == 1
    assert find_middle([2, 1, 1]) == 2
    assert find_middle([2, 1, 1]) == 2
    assert find_middle([1, 2, 2, 2, 1, 1]) == 5


def test_exercise_1():
    assert exercise_1(data_small) == 405


def test_exercise_1_full_data():
    assert exercise_1(data_full) == 27505
