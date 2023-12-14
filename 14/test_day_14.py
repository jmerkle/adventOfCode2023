from functions_day_14 import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')


def test_tilt_line():
    line = as_matrix(["O....#....##.O.O.##"])

    expected = as_matrix(["....O#....##...OO##"])

    assert (tilt_line(line) == expected).all()


def test_rotate_matrix_so_direction_is_right():
    platform = as_matrix([
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    ])

    rotated = rotate_matrix_so_direction_points_right(platform, "n")

    assert platform[0, 0] == rotated[0, -1] == "O"
    assert platform[0, -1] == rotated[-1, -1] == "."
    assert platform[-1, 0] == rotated[0, 0] == "#"
    assert platform[-1, -1] == rotated[-1, 0] == "."


def test_tilt_platform():
    platform = as_matrix([
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    ])

    expected = as_matrix([
        "OOOO.#.O..",
        "OO..#....#",
        "OO..O##..O",
        "O..#.OO...",
        "........#.",
        "..#....#.#",
        "..O..#.O.O",
        "..O.......",
        "#....###..",
        "#....#....",
    ])

    assert (tilt_platform(platform, "n") == expected).all()


def test_exercise_1():
    assert exercise_1(data_small) == 136
