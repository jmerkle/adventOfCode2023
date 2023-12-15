from typing import Optional, TypeAlias


def read_file_and_split_on_comma(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    lines = [x for x in data.split("\n") if len(x) > 0]
    return lines[0].split(",")


def hash_function(input_string: str) -> int:
    current_value = 0
    for c in list(input_string):
        current_value = (current_value + ord(c))*17 % 256
    return current_value


def exercise_1(data: list[str]) -> int:
    return sum(list(map(hash_function, data)))


def box_and_operation(step_input: str) -> tuple[int, Optional[int]]:
    if step_input[-1] == "-":
        return hash_function(step_input[:-1]), None
    label, focal_length = step_input.split("=")
    return hash_function(label), int(focal_length)

LabeledLens: TypeAlias = tuple[str, int]
Box: TypeAlias = list[LabeledLens]


def find_labeled_lens_in_box(box: Box, label: str) -> Optional[int]:
    return next((i for i, existing_lens in enumerate(box) if existing_lens[0] == label), None)


def remove_from_box(box: Box, label: str) -> Box:
    index_of_lens_with_label = find_labeled_lens_in_box(box, label)
    if index_of_lens_with_label is not None:
        del(box[index_of_lens_with_label])
    return box


def add_to_box(box: Box, lens: LabeledLens) -> Box:
    index_of_lens_with_label = find_labeled_lens_in_box(box, lens[0])
    if index_of_lens_with_label is None:
        box.append(lens)
    else:
        box[index_of_lens_with_label] = lens
    return box


def perform_step(boxes: list[Box], step_input: str) -> list[list[str]]:
    return []


def focal_power(boxes: list[Box]) -> int:
    return 0


def exercise_2(data: list[str]) -> int:
    boxes = [[] for _ in range(256)]
    for step_input in data:
        boxes = perform_step(boxes, step_input)
    return focal_power(boxes)
