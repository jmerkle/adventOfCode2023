from functions_day_19 import *

data_small = read_file_as_list_of_sections('input_small.txt')
data_full = read_file_as_list_of_sections('input.txt')


def test_read_file():
    workflows, parts = data_small
    assert workflows[0] == "px{a<2006:qkq,m>2090:A,rfg}"
    assert workflows[-1] == "hdj{m>838:A,pv}"
    assert parts[0] == "{x=787,m=2655,a=1222,s=2876}"
    assert parts[-1] == "{x=2127,m=1623,a=2188,s=1013}"


def test_parse_single_workflow():
    assert parse_single_workflow("px{a<2006:qkq,m>2090:A,rfg}") == ("px", ["a<2006:qkq", "m>2090:A", "rfg"])


def test_parse_workflows_as_dict():
    workflows, _ = data_small
    assert parse_workflows(workflows) == {
        "px": ["a<2006:qkq", "m>2090:A", "rfg"],
        "pv": ["a>1716:R", "A"],
        "lnx": ["m>1548:A", "A"],
        "rfg": ["s<537:gd", "x>2440:R", "A"],
        "qs": ["s>3448:A", "lnx"],
        "qkq": ["x<1416:A", "crn"],
        "crn": ["x>2662:A", "R"],
        "in": ["s<1351:px", "qqz"],
        "qqz": ["s>2770:qs", "m<1801:hdj", "R"],
        "gd": ["a>3333:R", "R"],
        "hdj": ["m>838:A", "pv"],
    }


def test_parse_parts():
    _, parts = data_small
    assert list(map(parse_part, parts)) == [
        (787, 2655, 1222, 2876),
        (1679, 44, 2067, 496),
        (2036, 264, 79, 2244),
        (2461, 1339, 466, 291),
        (2127, 1623, 2188, 1013),
    ]


def test_rate_part():
    assert rate_part((787, 2655, 1222, 2876)) == 7540


def test_apply_workflow_to_part():
    workflow = (["s<1351:px", "qqz"])
    assert apply_workflow_to_part(workflow, (787, 2655, 1222, 2876)) == "qqz"
    assert apply_workflow_to_part(workflow, (1679, 44, 2067, 496)) == "px"


def test_apply_all_workflows_to_part():
    workflows = {
        "px": ["a<2006:qkq", "m>2090:A", "rfg"],
        "pv": ["a>1716:R", "A"],
        "lnx": ["m>1548:A", "A"],
        "rfg": ["s<537:gd", "x>2440:R", "A"],
        "qs": ["s>3448:A", "lnx"],
        "qkq": ["x<1416:A", "crn"],
        "crn": ["x>2662:A", "R"],
        "in": ["s<1351:px", "qqz"],
        "qqz": ["s>2770:qs", "m<1801:hdj", "R"],
        "gd": ["a>3333:R", "R"],
        "hdj": ["m>838:A", "pv"],
    }
    assert apply_all_workflows_to_part(workflows, (787, 2655, 1222, 2876))
    assert not apply_all_workflows_to_part(workflows, (1679, 44, 2067, 496))


def test_exercise_1():
    assert exercise_1(data_small) == 19114


def test_exercise_1_full():
    assert exercise_1(data_full) == 391132


def test_calculate_distinct_combinations():
    workflows = {
        "px": ["a<2006:qkq", "m>2090:A", "rfg"],
        "pv": ["a>1716:R", "A"],
        "lnx": ["m>1548:A", "A"],
        "rfg": ["s<537:gd", "x>2440:R", "A"],
        "qs": ["s>3448:A", "lnx"],
        "qkq": ["x<1416:A", "crn"],
        "crn": ["x>2662:A", "R"],
        "in": ["s<1351:px", "qqz"],
        "qqz": ["s>2770:qs", "m<1801:hdj", "R"],
        "gd": ["a>3333:R", "R"],
        "hdj": ["m>838:A", "pv"],
        "test": ["A"]
    }
    assert calculate_distinct_combinations(workflows, ["A"], ((1, 2), (1, 1000), (1, 1000), (5, 10))) == 2*1000*1000*6
    assert calculate_distinct_combinations(workflows, ["R"], ((1, 2), (1, 1000), (1, 1000), (5, 10))) == 0
    assert calculate_distinct_combinations(workflows, ["test"], ((1, 2), (1, 1000), (1, 1000), (5, 10))) == 2*1000*1000*6
    assert calculate_distinct_combinations(workflows, ["test"], ((1, 2), (1, 1000), (-1, -1), (5, 10))) == 0


def test_split_ranges_on_predicate():
    assert (split_ranges_on_predicate("a<2006", ((1, 2), (1, 1000), (2000, 2010), (5, 10))) ==
            ((1, 2), (1, 1000), (2000, 2005), (5, 10)), ((1, 2), (1, 1000), (2006, 2010), (5, 10)))
    assert (split_ranges_on_predicate("a>2006", ((1, 2), (1, 1000), (2000, 2010), (5, 10))) ==
            ((1, 2), (1, 1000), (2007, 2010), (5, 10)), ((1, 2), (1, 1000), (2000, 2006), (5, 10)))
    assert (split_ranges_on_predicate("a>2006", ((1, 2), (1, 1000), (2000, 2001), (5, 10))) ==
            ((1, 2), (1, 1000), (-1, -1), (5, 10)), ((1, 2), (1, 1000), (2000, 2001), (5, 10)))
    assert (split_ranges_on_predicate("a>2006", ((1, 2), (1, 1000), (2007, 2010), (5, 10))) ==
            ((1, 2), (1, 1000), (2007, 2010), (5, 10)), ((1, 2), (1, 1000), (-1, -1), (5, 10)))


def test_exercise_2():
    assert exercise_2(data_small) == 167409079868000


def test_exercise_2_full():
    assert exercise_2(data_full) == 128163929109524
