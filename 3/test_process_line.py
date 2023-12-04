from functions import *
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

