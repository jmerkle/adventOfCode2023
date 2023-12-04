from functions import *

data_small = """467..114..
...*......
..35..633."""


def test_find_surrounding_symbols():
    data = """467..114..
            ...*......
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598.."""

    data = """467.\n...*"""

    result = surrounding_symbols_of_numerical_values(data)

    print(result)

    assert (result == np.array([
        [False, False, True, True],
        [False, False, True, False]
    ])).all()


def test_is_symbol():
    assert is_symbol("#")
    assert is_symbol("*")
    assert is_symbol("@")
    assert is_symbol("-")
    assert not is_symbol(".")
    assert not is_symbol("0")
    assert not is_symbol("1")
    assert not is_symbol("9")


def test_find_position_of_number():
    data = "467..114.."

    result = find_numbers_with_position_indexes(data)

    assert result[0] == [467, 0, 3]
    assert result[1] == [114, 5, 8]
    assert len(result) == 2


def test_find_adjacent_gears_for_found_number():
    data = data_small.split("\n")

    found_number1 = [467, 0, 3]
    found_number2 = [35, 2, 4]

    result1 = find_adjacent_gear_for_found_number(data, 0, found_number1)
    result2 = find_adjacent_gear_for_found_number(data, 2, found_number2)

    assert result1 == ["1-3"]
    assert result2 == ["1-3"]


def test_find_adjacent_gear_for_position():
    matrix = data_small.split("\n")

    result = find_adjacent_gear_for_position(matrix, 0, 2)
    assert result == ["1-3"]


def test_find_multiple_adjacent_gears_for_position():
    matrix = """467*.114..
...*......
..35..633.""".split("\n")

    result = find_adjacent_gear_for_position(matrix, 0, 2)
    assert result == ["0-3", "1-3"]


def test_create_dictionary_for_found_gears():
    dict1 = findings_as_dictionary(467, ["1-3"])
    dict2 = findings_as_dictionary(35, ["1-3", "2-4"])

    assert dict1 == {
        "1-3": [467]
    }
    assert dict2 == {
        "1-3": [35],
        "2-4": [35]
    }

def test_merge_dictionaries():
    dict1 = {
        "1-3": [467]
    }
    dict2 = {
        "1-3": [35],
        "2-4": [35]
    }

    merged = merge_dictionaries(dict1, dict2)

    assert merged == {
        "1-3": [467, 35],
        "2-4": [35]
    }
