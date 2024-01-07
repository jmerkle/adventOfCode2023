from enum import IntEnum
from typing import TypeAlias


def read_file_as_list_of_sections(filename: str) -> list[list[str]]:
    f = open(filename, 'r')
    data = f.read()
    f.close()
    sections = [x.strip() for x in data.split("\n\n") if len(x) > 0]
    return [x.split("\n") for x in sections if len(x) > 0]


class Categories(IntEnum):
    x = 0
    m = 1
    a = 2
    s = 3


Part: TypeAlias = tuple[int, int, int, int]


def parse_single_workflow(workflow_as_string: str) -> tuple[str, list[str]]:
    name, instructions = workflow_as_string.removesuffix("}").split("{")
    return name, instructions.split(",")


def parse_workflows(workflows_as_strings: list[str]) -> dict[str, list[str]]:
    return dict(map(parse_single_workflow, workflows_as_strings))


def exercise_1(data: list[list[str]]) -> int:
    return 0
