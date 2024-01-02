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


def test_draw_down():
    command = (Direction.DOWN, 5, 0X0dc571)
    grid = [["."]]
    position = (0, 0)
    assert draw(grid, position, command) == ([["#"], ["#"], ["#"], ["#"], ["#"], ["#"]], (5, 0))


def test_draw_left():
    command = (Direction.LEFT, 2, 0X70c710)
    grid = [[".", ".", "."]]
    position = (0, 2)
    assert draw(grid, position, command) == ([["#", "#", "#"]], (0, 0))


def test_draw_up():
    command = (Direction.UP, 1, 0X70c710)
    grid = [["."], ["."], ["."]]
    position = (2, 0)
    assert draw(grid, position, command) == ([["."], ["#"], ["#"]], (1, 0))


def test_resize_new_grid_right():
    grid = [["."]]
    grid = resize_right(grid, 5)
    assert grid == [[".", ".", ".", ".", ".", "."]]


def test_resize_existing_grid_right():
    grid = [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"]
            ]
    grid = resize_right(grid, 2)
    assert grid == [
        ["#", "#", "#", ".", "."],
        ["#", ".", "#", ".", "."],
        ["#", ".", "#", ".", "."],
        ["#", "#", "#", ".", "."]
    ]


def test_resize_new_grid_down():
    grid = [["."]]
    grid = resize_down(grid, 5)
    assert grid == [["."], ["."], ["."], ["."], ["."], ["."]]


def test_resize_existing_grid_down():
    grid = [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"]
    ]
    grid = resize_down(grid, 2)
    assert grid == [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"],
        [".", ".", "."],
        [".", ".", "."]
    ]


def test_resize_existing_grid_left():
    grid = [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"]
    ]
    grid = resize_left(grid, 2)
    assert grid == [
        [".", ".", "#", "#", "#"],
        [".", ".", "#", ".", "#"],
        [".", ".", "#", ".", "#"],
        [".", ".", "#", "#", "#"]
    ]


def test_resize_existing_grid_up():
    grid = [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"]
    ]
    grid = resize_up(grid, 2)
    assert grid == [
        [".", ".", "."],
        [".", ".", "."],
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"]
    ]


def test_find_inner_point_left_edge():
    grid = [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"]
    ]
    assert find_inner_point(grid) == (1, 1)

def test_find_inner_point_middle():
    grid = [
        [".", "#", "#", "#", "."],
        [".", "#", ".", "#", "."],
        [".", "#", ".", "#", "."],
        [".", "#", "#", "#", "."]
    ]
    assert find_inner_point(grid) == (1, 2)


def test_exercise_1():
    assert exercise_1(data_small) == 62


def test_exercise_1_full():
    assert exercise_1(data_full) == 45159
