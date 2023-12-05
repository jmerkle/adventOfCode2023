from functions_day_5 import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')


def test_read_file():
    sections = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
    assert len(sections) == 8
    assert sections[0] == "seeds: 79 14 55 13"
    assert sections[1] == """seed-to-soil map:
50 98 2
52 50 48"""
    assert sections[-1] == """humidity-to-location map:
60 56 37
56 93 4"""


def test_parse_mapping():
    mapping_as_text = """seed-to-soil map:
50 98 2
52 50 48"""

    parsed = parse_mapping(mapping_as_text)

    assert parsed == [[50, 98, 2], [52, 50, 48]]


def test_find_value_in_mapping():
    mapping = [[50, 98, 2], [52, 50, 48]]

    assert find_value_in_mapping(mapping, 79) == 81
    assert find_value_in_mapping(mapping, 14) == 14
    assert find_value_in_mapping(mapping, 55) == 57
    assert find_value_in_mapping(mapping, 13) == 13


def test_chain_mappings():
    mapping1 = [[50, 98, 2], [52, 50, 48]]
    mapping2 = [[0, 15, 37], [37, 52, 2], [39, 0, 15]]
    mapping3 = [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]]

    assert value_from_chained_mappings([mapping1, mapping2, mapping3], 14) == 49


def test_exercise_1():
    assert exercise_1(data_small) == 35
