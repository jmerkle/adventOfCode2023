from functions_day_17 import *

data_small = read_file_as_list_of_list_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_list_of_list_and_filter_empty_lines('input.txt')


def test_possible_movements():
    grid = [[2, 4, 1],
            [3, 2, 1],
            [3, 2, 5]]

    assert (calculate_possible_movements(grid, (0, 0, Direction.RIGHT, 0)) ==
            {
                (0, 1, Direction.RIGHT, 1): 4,
                (1, 0, Direction.DOWN, 1): 3
            })

    assert (calculate_possible_movements(grid, (1, 1, Direction.UP, 2)) ==
            {
                (0, 1, Direction.UP, 3): 4,
                (1, 2, Direction.RIGHT, 1): 1,
                (1, 0, Direction.LEFT, 1): 3
            })

    assert (calculate_possible_movements(grid, (1, 1, Direction.UP, 3)) ==
            {
                (1, 2, Direction.RIGHT, 1): 1,
                (1, 0, Direction.LEFT, 1): 3
            })


def test_exercise_1():
    assert exercise_1(data_small) == 102
