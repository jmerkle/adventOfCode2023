from functions_day_15 import *

data_small = read_file_and_split_on_comma('input_small.txt')
data_full = read_file_and_split_on_comma('input.txt')


def test_hash():
    assert hash_function("HASH") == 52
    assert hash_function("rn=1") == 30
    assert hash_function("cm-") == 253


def test_exercise_1():
    assert exercise_1(data_small) == 1320


def test_exercise_1_full_data():
    assert exercise_1(data_full) == 511498
