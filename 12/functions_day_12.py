import re
import itertools


def read_file_as_list_of_lines_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


def unfold_record(line: str) -> str:
    factor = 5
    record, check_values = line.split(" ")
    unfolded_record = "?".join([record] * factor)
    unfolded_check_values = ",".join([check_values] * factor)
    return unfolded_record + " " + unfolded_check_values


def record_could_start_with(record: str, check_value: int) -> bool:
    if "." not in record[0:check_value]:
        if len(record) > check_value and record[check_value] == "#":
            return False
        return True
    return False


def generate_possible_remaining_records(record: str, check_value: int) -> list[str]:
    if len(record) < check_value:
        return []
    if len(record) == check_value:
        if record_could_start_with(record, check_value):
            return [""]
        else:
            return []
    remaining = []
    if record_could_start_with(record, check_value):
        remaining = [record[check_value+1:]]
    if record[0] == "#":
        return remaining
    else:
        return remaining + generate_possible_remaining_records(record[1:], check_value)


def count_possible_arrangements(line: str) -> int:
    record, check_values_str = remove_duplicate_dots(line).split(" ")
    check_values = [int(c) for c in check_values_str.split(",")]
    possible_remaining_records = generate_possible_remaining_records(record, check_values[0])
    if len(check_values) == 1:
        return len(list(filter(lambda r: "#" not in r, possible_remaining_records)))
    counter = 0
    for r in possible_remaining_records:
        counter += count_possible_arrangements(r + " " + ",".join([str(i) for i in check_values[1:]]))
    return counter


def remove_duplicate_dots(line: str) -> str:
    while line.replace("..", ".") != line:
        line = line.replace("..", ".")
    return line


def exercise_1(data: list[str]) -> int:
    return sum(list(map(count_possible_arrangements, data)))


def exercise_2(data: list[str]) -> int:
    unfolded_data = list(map(unfold_record, data))
    return sum(list(map(count_possible_arrangements, unfolded_data)))
