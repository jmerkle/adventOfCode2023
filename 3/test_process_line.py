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

# def test_find_adjacent_gears_for_found_number():
#     data = """467..114..
# ...*......
# ..35..633."""
#
#     found_number = [467, 0, 3]
#     line = 0
#
#     result = find_adjacent_gear_for_found_number(data, line, found_number)
#
#     assert result == ["1-3", 467]

def test_find_adjacent_gear_for_position():
    matrix = data_small.split("\n")

    result = find_adjacent_gear_for_position(matrix, 0, 2)
    assert result == ["1-3"]


def test_find_multiple_adjacent_gears_for_position():
    matrix = """467*.114..
...*......
..35..633.""" .split("\n")

    result = find_adjacent_gear_for_position(matrix, 0, 2)
    assert result == ["0-3", "1-3"]
