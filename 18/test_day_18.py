from functions_day_18 import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')


def test_parse_command():
    assert parse_command("R 6 (#70c710)") == (Direction.RIGHT, 6, 0X70c710)


def test_draw_right():
    command = (Direction.RIGHT, 6, 0X70c710)
    grid = [["."]]
    position = (0, 0)
    assert draw(grid, position, command) == ([["#", "#", "#", "#", "#", "#", "#"]], (0, 6))


def test_resize_new_grid_right():
    grid = [["."]]
    resize_right(grid, 5)
    assert grid == [[".", ".", ".", ".", ".", "."]]


def test_resize_existing_grid_right():
    grid = [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"]
            ]
    resize_right(grid, 2)
    assert grid == [
        ["#", "#", "#", ".", "."],
        ["#", ".", "#", ".", "."],
        ["#", ".", "#", ".", "."],
        ["#", "#", "#", ".", "."]
    ]


def test_resize_new_grid_down():
    grid = [["."]]
    resize_down(grid, 5)
    assert grid == [["."], ["."], ["."], ["."], ["."], ["."]]


def test_resize_existing_grid_down():
    grid = [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"]
    ]
    resize_down(grid, 2)
    assert grid == [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"],
        [".", ".", "."],
        [".", ".", "."]
    ]


def test_exercise_1():
    assert exercise_1(data_small) == 62
