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


def test_new_direction():
    # dot
    assert calculate_new_directions(".", Direction.RIGHT) == [Direction.RIGHT]
    assert calculate_new_directions(".", Direction.DOWN) == [Direction.DOWN]
    assert calculate_new_directions(".", Direction.LEFT) == [Direction.LEFT]
    assert calculate_new_directions(".", Direction.UP) == [Direction.UP]
    # slash
    assert calculate_new_directions("/", Direction.RIGHT) == [Direction.UP]
    assert calculate_new_directions("/", Direction.DOWN) == [Direction.LEFT]
    assert calculate_new_directions("/", Direction.LEFT) == [Direction.DOWN]
    assert calculate_new_directions("/", Direction.UP) == [Direction.RIGHT]
    # backslash
    assert calculate_new_directions("\\", Direction.RIGHT) == [Direction.DOWN]
    assert calculate_new_directions("\\", Direction.DOWN) == [Direction.RIGHT]
    assert calculate_new_directions("\\", Direction.LEFT) == [Direction.UP]
    assert calculate_new_directions("\\", Direction.UP) == [Direction.LEFT]
    # dash
    assert calculate_new_directions("-", Direction.RIGHT) == [Direction.RIGHT]
    assert calculate_new_directions("-", Direction.DOWN) == [Direction.RIGHT, Direction.LEFT]
    assert calculate_new_directions("-", Direction.LEFT) == [Direction.LEFT]
    assert calculate_new_directions("-", Direction.UP) == [Direction.RIGHT, Direction.LEFT]
    # pipe
    assert calculate_new_directions("|", Direction.RIGHT) == [Direction.UP, Direction.DOWN]
    assert calculate_new_directions("|", Direction.DOWN) == [Direction.DOWN]
    assert calculate_new_directions("|", Direction.LEFT) == [Direction.UP, Direction.DOWN]
    assert calculate_new_directions("|", Direction.UP) == [Direction.UP]

def test_symbol_on_grid():
    #dot
    assert calculate_more_movements([[".", "."]], (Direction.RIGHT, (0, 0))) == [(Direction.RIGHT, (0, 1))]
    assert calculate_more_movements([[".", "."]], (Direction.LEFT, (0, 1))) == [(Direction.LEFT, (0, 0))]
    assert calculate_more_movements([["."], ["."]], (Direction.DOWN, (0, 0))) == [(Direction.DOWN, (1, 0))]
    assert calculate_more_movements([["."], ["."]], (Direction.UP, (1, 0))) == [(Direction.UP, (0, 0))]

    assert calculate_more_movements([["."]], (Direction.RIGHT, (0, 0))) == []
    assert calculate_more_movements([["."]], (Direction.LEFT, (0, 0))) == []
    assert calculate_more_movements([["."]], (Direction.DOWN, (0, 0))) == []
    assert calculate_more_movements([["."]], (Direction.UP, (0, 0))) == []

    #slash
    assert calculate_more_movements([["."], ["/"]], (Direction.RIGHT, (1, 0))) == [(Direction.UP, (0, 0))]
    assert calculate_more_movements([[".", "/"]], (Direction.DOWN, (0, 1))) == [(Direction.LEFT, (0, 0))]
    assert calculate_more_movements([["/"], ["."]], (Direction.LEFT, (0, 0))) == [(Direction.DOWN, (1, 0))]
    assert calculate_more_movements([["/", "."]], (Direction.UP, (0, 0))) == [(Direction.RIGHT, (0, 1))]

    #backslash
    assert calculate_more_movements([["\\"], ["."]], (Direction.RIGHT, (0, 0))) == [(Direction.DOWN, (1, 0))]

    #dash
    assert calculate_more_movements([["."], ["|"], ["."]], (Direction.RIGHT, (1, 0))) == [(Direction.UP, (0, 0)), (Direction.DOWN, (2, 0))]
    assert calculate_more_movements([["|"], ["."]], (Direction.RIGHT, (0, 0))) == [(Direction.DOWN, (1, 0))]


def test_exercise_1():
    assert exercise_1(data_small) == 46


def test_exercise_1_full():
    assert exercise_1(data_full) == 7951
