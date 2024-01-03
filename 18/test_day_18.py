from functions_day_18 import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')


def test_parse_command():
    assert parse_command("R 6 (#70c710)") == (Direction.RIGHT, 6)


def test_dictionary_horizontal_edge():
    d = {
        0: [0],
        1: [4]
    }
    edge = (1, range(0, 4))
    assert insert_edge(d, edge) == {
        0: [0],
        1: [0, 1, 2, 3, 4]
    }


def test_dictionary_horizontal_edge_merge():
    d = {
        0: [3]
    }
    edge = (0, range(0, 4))
    assert insert_edge(d, edge) == {
        0: [0, 1, 2, 3, 3]
    }


def test_dictionary_vertical_edge():
    d = {
        1: [0]
    }
    edge = (0, range(0, 1))
    assert insert_edge(d, edge) == {
        0: [0],
        1: [0]
    }


def test_draw_right():
    command = (Direction.RIGHT, 6)
    edge_dictionary = {}
    position = (0, 0)
    edge_dictionary, position = draw(edge_dictionary, position, command)
    assert edge_dictionary == {
        0: [0, 1, 2, 3, 4, 5]
    }
    assert position == (0, 6)


def test_draw_down():
    command = (Direction.DOWN, 5)
    edge_dictionary = {}
    position = (0, 0)
    edge_dictionary, position = draw(edge_dictionary, position, command)
    assert edge_dictionary == {
        0: [0],
        1: [0],
        2: [0],
        3: [0],
        4: [0]
    }
    assert position == (5, 0)


def test_draw_left():
    command = (Direction.LEFT, 2)
    edge_dictionary = {}
    position = (0, 2)
    edge_dictionary, position = draw(edge_dictionary, position, command)
    assert edge_dictionary == {
        0: [1, 2]
    }
    assert position == (0, 0)


def test_draw_up():
    command = (Direction.UP, 2)
    edge_dictionary = {}
    position = (2, 0)
    edge_dictionary, position = draw(edge_dictionary, position, command)
    assert edge_dictionary == {
        1: [0],
        2: [0]
    }
    assert position == (0, 0)


def test_resize_new_grid_right():
    grid = np.array([[0]])
    grid = resize_right(grid, 5)
    assert (grid == np.array([0, 0, 0, 0, 0, 0])).all()


def test_resize_existing_grid_right():
    grid = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
            ])
    grid = resize_right(grid, 2)
    assert (grid == [
        [1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0]
    ]).all()


def test_resize_new_grid_down():
    grid = np.array([[0]])
    grid = resize_down(grid, 5)
    assert (grid == [
        [0],
        [0],
        [0],
        [0],
        [0],
        [0]
    ]).all()


def test_resize_existing_grid_down():
    grid = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    grid = resize_down(grid, 2)
    assert (grid == np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ])).all()


def test_resize_existing_grid_left():
    grid = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    grid = resize_left(grid, 2)
    assert (grid == [
        [0, 0, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 1, 1]
    ]).all()


def test_resize_existing_grid_up():
    grid = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    grid = resize_up(grid, 2)
    assert (grid == np.array([
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])).all()


def test_find_inner_point_left_edge():
    grid = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    assert find_inner_point(grid) == (1, 1)


def test_find_inner_point_middle():
    grid = np.array([
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0]
    ])
    assert find_inner_point(grid) == (1, 2)


def test_exercise_1():
    assert exercise_1(data_small) == 62


def test_exercise_1_full():
    assert exercise_1(data_full) == 45159


def test_convert_hex_to_command():
    assert hex_to_command("R 6 (#70c710)") == (Direction.RIGHT, 461937)
    assert hex_to_command("D 5 (#0dc571)") == (Direction.DOWN, 56407)
    assert hex_to_command("L 5 (#8ceee2)") == (Direction.LEFT, 577262)
    assert hex_to_command("U 2 (#caa173)") == (Direction.UP, 829975)


def test_exercise_2():
    assert exercise_2(data_small) == 952408144115
