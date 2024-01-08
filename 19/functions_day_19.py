import re
from typing import TypeAlias
import numpy


def read_file_as_list_of_sections(filename: str) -> list[list[str]]:
    f = open(filename, 'r')
    data = f.read()
    f.close()
    sections = [x.strip() for x in data.split("\n\n") if len(x) > 0]
    return [x.split("\n") for x in sections if len(x) > 0]


category_indexes = {
    "x": 0,
    "m": 1,
    "a": 2,
    "s": 3,
}


Workflow: TypeAlias = tuple[str, list[str]]
Part: TypeAlias = tuple[int, int, int, int]
PartRanges: TypeAlias = tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]


def parse_single_workflow(workflow_as_string: str) -> Workflow:
    name, instructions = workflow_as_string.removesuffix("}").split("{")
    return name, instructions.split(",")


def parse_workflows(workflows_as_strings: list[str]) -> dict[str, list[str]]:
    return dict(map(parse_single_workflow, workflows_as_strings))


def parse_part(part_as_string: str) -> Part:
    values = re.search("{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", part_as_string)
    return int(values.group(1)), int(values.group(2)), int(values.group(3)), int(values.group(4))


def rate_part(part: Part) -> int:
    return sum(part)


def apply_predicate_to_part(predicate: str, part: Part) -> bool:
    category, comparator, *_ = list(predicate)
    value_int = int(predicate[2:])
    part_value = part[category_indexes.get(category)]
    if comparator == ">":
        return part_value > value_int
    return part_value < value_int


def apply_workflow_to_part(workflow: list[str], part: Part) -> str:
    first_rule, *remaining_rules = workflow
    if ":" not in first_rule:
        return first_rule
    predicate, next_workflow = first_rule.split(":")
    if apply_predicate_to_part(predicate, part):
        return next_workflow
    else:
        return apply_workflow_to_part(remaining_rules, part)


def apply_all_workflows_to_part(workflows: dict[str, list[str]], part: Part) -> bool:
    current_workflow = []
    result = "in"
    while result not in ["A", "R"]:
        current_workflow = workflows.get(result)
        result = apply_workflow_to_part(current_workflow, part)
    return result == "A"


def exercise_1(data: list[list[str]]) -> int:
    workflows = parse_workflows(data[0])
    parts = map(parse_part, data[1])
    accepted_parts = filter(lambda p: apply_all_workflows_to_part(workflows, p), parts)
    return sum(map(rate_part, accepted_parts))


def distinct_combinations_in_range(part_ranges: PartRanges):
    return numpy.prod(list(map(lambda r: r[1] - r[0] + 1, part_ranges)))


def split_range_on_less(category_range: tuple[int, int], split_value: int) -> tuple[tuple[int, int], tuple[int, int]]:
    lower, upper = category_range
    if upper < split_value:
        return category_range, (-1, -1)
    if lower >= split_value:
        return (-1, -1), category_range
    return (lower, split_value - 1), (split_value, upper)


def split_range_on_greater(category_range: tuple[int, int], split_value: int) -> tuple[tuple[int, int], tuple[int, int]]:
    lower, upper = category_range
    if lower > split_value:
        return category_range, (-1, -1)
    if upper <= split_value:
        return (-1, -1), category_range
    return (split_value + 1, upper), (lower, split_value)


def split_ranges_on_predicate(predicate: str, part_ranges: PartRanges) -> tuple[PartRanges, PartRanges]:
    category, comparator, *_ = list(predicate)
    value_int = int(predicate[2:])
    category_index = category_indexes.get(category)
    if comparator == "<":
        matching, remaining = split_range_on_less(part_ranges[category_index], value_int)
    else:
        matching, remaining = split_range_on_greater(part_ranges[category_index], value_int)
    m_l = list(part_ranges)
    m_l[category_index] = matching
    r_l = list(part_ranges)
    r_l[category_index] = remaining
    return tuple(m_l), tuple(r_l)


def calculate_distinct_combinations(workflows: dict[str, list[str]], current_workflow: list[str], part_ranges: PartRanges) -> int:
    if (-1, -1) in part_ranges:
        return 0
    first_rule, *remaining_rules = current_workflow
    if first_rule == "A":
        return distinct_combinations_in_range(part_ranges)
    if first_rule == "R":
        return 0
    if ":" not in first_rule:
        new_workflow = workflows.get(first_rule)
        return calculate_distinct_combinations(workflows, new_workflow, part_ranges)
    predicate, next_workflow = first_rule.split(":")
    matching_range, remaining_range = split_ranges_on_predicate(predicate, part_ranges)
    return (calculate_distinct_combinations(workflows, [next_workflow], matching_range) +
            calculate_distinct_combinations(workflows, remaining_rules, remaining_range))


def exercise_2(data: list[list[str]]) -> int:
    workflows = parse_workflows(data[0])
    starting_workflow = workflows.get("in")
    return calculate_distinct_combinations(workflows, starting_workflow, ((1, 4000), (1, 4000), (1, 4000), (1, 4000)))
