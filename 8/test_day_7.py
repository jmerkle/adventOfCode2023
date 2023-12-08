from functions_day_7 import *

data_small_1 = read_file_as_instructions_and_maps('input_small_1.txt')
data_small_2 = read_file_as_instructions_and_maps('input_small_2.txt')
data_full = read_file_as_instructions_and_maps('input.txt')


def test_read_file():
    instructions, maps = data_small_2
    assert instructions == "LLR"
    assert maps[0] == "AAA = (BBB, BBB)"
    assert maps[-1] == "ZZZ = (ZZZ, ZZZ)"


def test_exercise_1():
    assert exercise_1(data_small_1) == 2
    assert exercise_1(data_small_2) == 6

# def test_exercise_1_all_data():
#     print(exercise_1(data_full))
