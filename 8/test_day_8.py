from functions_day_8 import *

data_small_1 = read_file_as_instructions_and_maps('input_small_1.txt')
data_small_2 = read_file_as_instructions_and_maps('input_small_2.txt')
data_small_exercise_2 = read_file_as_instructions_and_maps('input_small_exercise_2.txt')
data_full = read_file_as_instructions_and_maps('input.txt')


def test_read_file():
    instructions, maps = data_small_2
    assert instructions == "LLR"
    assert maps[0] == "AAA = (BBB, BBB)"
    assert maps[-1] == "ZZZ = (ZZZ, ZZZ)"


def test_map_to_triple():
    assert map_to_triple("AAA = (BBB, CCC)") == ("AAA", "BBB", "CCC")


def test_maps_as_dictionary():
    assert maps_as_dictionary(data_small_2[1]) == {
        "AAA": ("BBB", "BBB"),
        "BBB": ("AAA", "ZZZ"),
        "ZZZ": ("ZZZ", "ZZZ"),
    }


def test_exercise_1():
    assert exercise_1(data_small_1) == 2
    assert exercise_1(data_small_2) == 6


def test_exercise_1_all_data():
    assert exercise_1(data_full) == 19951


def test_find_repeating_destinations():
    instructions, maps_raw = data_small_exercise_2
    maps: dict[str, tuple[str, str]] = maps_as_dictionary(maps_raw)
    result1 = find_repeating_destinations(maps, instructions, "11A")
    assert result1[0] == (2, 2)

    result2 = find_repeating_destinations(maps, instructions, "22A")
    assert result2[0] == (3, 6)
    assert result2[1] == (6, 6)


def test_exercise_2():
    assert exercise_2(data_small_exercise_2) == 6


def test_exercise_2_all_data():
    print(exercise_2(data_full))
