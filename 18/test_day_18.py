from functions_day_18 import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')


def test_parse_command():
    assert parse_command("R 6 (#70c710)") == (Direction.RIGHT, 6)


def test_dictionary_edge():
    d = {
        0: [0],
        1: [4]
    }
    edge = (1, range(0, 4))
    assert insert_edge(d, edge) == {
        0: [0],
        1: [0, 1, 2, 3, 4]
    }


def test_dictionary_edge_merge():
    d = {
        0: [3]
    }
    edge = (0, range(0, 4))
    assert insert_edge(d, edge) == {
        0: [0, 1, 2, 3, 3]
    }


def test_draw_right():
    command = (Direction.RIGHT, 6)
    horizontal_edges = {}
    vertical_edges = {}
    position = (0, 0)
    horizontal_edges, vertical_edges, position = draw(horizontal_edges, vertical_edges, position, command)
    assert horizontal_edges == {
        0: [0, 1, 2, 3, 4, 5]
    }
    assert vertical_edges == {}
    assert position == (0, 6)


def test_draw_down():
    command = (Direction.DOWN, 5)
    horizontal_edges = {}
    vertical_edges = {}
    position = (0, 0)
    horizontal_edges, vertical_edges, position = draw(horizontal_edges, vertical_edges, position, command)
    assert horizontal_edges == {}
    assert vertical_edges == {
        0: [0, 1, 2, 3, 4]
    }
    assert position == (5, 0)


def test_draw_left():
    command = (Direction.LEFT, 2)
    horizontal_edges = {}
    vertical_edges = {}
    position = (0, 2)
    horizontal_edges, vertical_edges, position = draw(horizontal_edges, vertical_edges, position, command)
    assert horizontal_edges == {
        0: [1, 2]
    }
    assert vertical_edges == {}
    assert position == (0, 0)


def test_draw_up():
    command = (Direction.UP, 2)
    horizontal_edges = {}
    vertical_edges = {}
    position = (2, 0)
    horizontal_edges, vertical_edges, position = draw(horizontal_edges, vertical_edges, position, command)
    assert horizontal_edges == {}
    assert vertical_edges == {
        0: [1, 2]
    }
    assert position == (0, 0)


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


def test_exercise_2_full():
    assert exercise_2(data_full) == 952408144115
