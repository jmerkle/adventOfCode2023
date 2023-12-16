from functions_day_16 import *

data_small = read_file_as_list_of_list_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_list_of_list_and_filter_empty_lines('input.txt')


def test_movement_queue():
    q = MovementQueue()
    movement_1 = Direction.RIGHT, (0, 0)
    movement_2 = Direction.LEFT, (0, 0)
    q.put(movement_1)
    q.put(movement_2)
    q.put(movement_1)

    result1 = q.get()
    result2 = q.get()
    result3 = q.get()
    assert result1 == movement_1
    assert result2 == movement_2
    assert result3 is None


def test_exercise_1():
    assert exercise_1(data_small) == 46
