from functions_day_12 import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')


def test_validate_arrangement():
    assert validate_arrangement("#.#.### 1,1,3") == True
    assert validate_arrangement("##..### 1,1,3") == False
    assert validate_arrangement(".###.##.#... 3,2,1") == True
    assert validate_arrangement(".###..##..#. 3,2,1") == True
    assert validate_arrangement(".###..###... 3,2,1") == False


def test_apply_arrangement():
    assert apply_arrangement("???.### 1,1,3", "101") == "#.#.### 1,1,3"


def test_find_arrangements():
    assert count_possible_arrangements("???.### 1,1,3") == 1
    assert count_possible_arrangements(".??..??...?##. 1,1,3") == 4
    assert count_possible_arrangements("?#?#?#?#?#?#?#? 1,3,1,6") == 1
    assert count_possible_arrangements("????.#...#... 4,1,1") == 1
    assert count_possible_arrangements("????.######..#####. 1,6,5") == 4
    assert count_possible_arrangements("?###???????? 3,2,1") == 10


def test_exercise_1():
    assert exercise_1(data_small) == 21


def test_exercise_1_full_data():
    assert exercise_1(data_full) == 7771
