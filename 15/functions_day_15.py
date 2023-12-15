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
        current_value = (current_value + ord(c)) * 17 % 256
    return current_value


def exercise_1(data: list[str]) -> int:
    return sum(list(map(hash_function, data)))


LabeledLens: TypeAlias = tuple[str, int]
Box: TypeAlias = list[LabeledLens]


def box_number_and_operation(step_input: str) -> tuple[int, str, Optional[int]]:
    if step_input[-1] == "-":
        return hash_function(step_input[:-1]), step_input[:-1], None
    label, focal_length = step_input.split("=")
    return hash_function(label), label, int(focal_length)


def find_labeled_lens_in_box(box: Box, label: str) -> Optional[int]:
    return next((i for i, existing_lens in enumerate(box) if existing_lens[0] == label), None)


def remove_from_box(box: Box, label: str) -> Box:
    index_of_lens_with_label = find_labeled_lens_in_box(box, label)
    if index_of_lens_with_label is not None:
        del (box[index_of_lens_with_label])
    return box


def add_to_box(box: Box, lens: LabeledLens) -> Box:
    index_of_lens_with_label = find_labeled_lens_in_box(box, lens[0])
    if index_of_lens_with_label is None:
        box.append(lens)
    else:
        box[index_of_lens_with_label] = lens
    return box


def perform_step(boxes: list[Box], step_input: str):
    box_number, label, focal_length = box_number_and_operation(step_input)
    if focal_length is None:
        remove_from_box(boxes[box_number], label)
    else:
        add_to_box(boxes[box_number], (label, focal_length))


def focal_power_box(box: Box, box_number: int) -> int:
    power = 0
    for slot in range(len(box)):
        power += (box_number + 1) * (slot + 1) * box[slot][1]
    return power


def focal_power(boxes: list[Box]) -> int:
    power = 0
    for b in range(len(boxes)):
        power += focal_power_box(boxes[b], b)
    return power


def exercise_2(data: list[str]) -> int:
    boxes = [[] for _ in range(256)]
    for step_input in data:
        perform_step(boxes, step_input)
    return focal_power(boxes)
