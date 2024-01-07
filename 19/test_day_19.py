from functions_day_19 import *

data_small = read_file_as_list_of_sections('input_small.txt')
data_full = read_file_as_list_of_sections('input.txt')


def test_read_file():
    workflows, parts = data_small
    assert workflows[0] == "px{a<2006:qkq,m>2090:A,rfg}"
    assert workflows[-1] == "hdj{m>838:A,pv}"
    assert parts[0] == "{x=787,m=2655,a=1222,s=2876}"
    assert parts[-1] == "{x=2127,m=1623,a=2188,s=1013}"


def test_exercise_1():
    assert exercise_1(data_small) == 19114
