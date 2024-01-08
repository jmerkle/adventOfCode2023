import re
from enum import Enum
from typing import TypeAlias


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


def parse_single_workflow(workflow_as_string: str) -> Workflow:
    name, instructions = workflow_as_string.removesuffix("}").split("{")
    return name, instructions.split(",")


def parse_workflows(workflows_as_strings: list[str]) -> dict[str, list[str]]:
    return dict(map(parse_single_workflow, workflows_as_strings))


def parse_part(part_as_string: str) -> Part:
    values = re.search("{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", part_as_string)
    return int(values.group(1)), int(values.group(2)), int(values.group(3)), int(values.group(4))


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
    return 0
