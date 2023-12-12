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


def generate_possible_remaining_records(record: str, check_value: int, min_size:int = 0) -> list[str]:
    if len(record) < check_value or len(record) < min_size:
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
        return remaining + generate_possible_remaining_records(record[1:], check_value, min_size)


def count_possible_arrangements_rec(line: str, computed_results: dict[str, int] = {}) -> tuple[int, dict[str, int]]:
    if line in computed_results:
        return computed_results[line], computed_results
    record, check_values_str = remove_duplicate_dots(line).split(" ")
    check_values = [int(c) for c in check_values_str.split(",")]
    if len(check_values) == 1:
        counter = len(list(filter(lambda r: "#" not in r, generate_possible_remaining_records(record, check_values[0]))))
        return counter, computed_results | {line: counter}
    min_remaining_size = sum(check_values[1:]) + len(check_values[1:])
    possible_remaining_records = generate_possible_remaining_records(record, check_values[0], min_remaining_size)
    counter = 0
    for r in possible_remaining_records:
        new_count, new_computed_results = count_possible_arrangements_rec(r + " " + ",".join([str(i) for i in check_values[1:]]), computed_results)
        counter += new_count
        computed_results = computed_results | new_computed_results
    return counter, computed_results | {line: counter}


def remove_duplicate_dots(line: str) -> str:
    while line.replace("..", ".") != line:
        line = line.replace("..", ".")
    return line


def count_possible_arrangements(line: str) -> int:
    return count_possible_arrangements_rec(line)[0]


def exercise_1(data: list[str]) -> int:
    return sum(list(map(count_possible_arrangements, data)))


def exercise_2(data: list[str]) -> int:
    unfolded_data = list(map(unfold_record, data))
    return sum(list(map(count_possible_arrangements, unfolded_data)))
