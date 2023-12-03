from validate_cubes import *


def test_validate_valid():
    available_cubes = {
        "blue": 14,
        "green": 13,
        "red": 12
    }
    shown_cubes = {
        "blue": 6,
        "green": 2,
        "red": 4
    }

    assert cubes_are_valid(available_cubes, shown_cubes)


def test_validate_invalid():
    available_cubes = {
        "blue": 14,
        "green": 13,
        "red": 12
    }
    shown_cubes = {
        "blue": 5,
        "green": 13,
        "red": 20
    }

    assert not cubes_are_valid(available_cubes, shown_cubes)
