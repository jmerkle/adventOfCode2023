import re
import itertools


def read_file_as_list_of_lines_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


def validate_arrangement(line: str) -> bool:
    record, check_values = line.split(" ")
    groups_of_hash = [len(group) for group in re.findall("#+", record)]
    check_values = [int(c) for c in check_values.split(",")]
    return groups_of_hash == check_values


def find_all_q(line: list[str]) -> list[int]:
    return [i for i in range(len(line)) if line[i] == "?"]


def apply_arrangement(line: str, arrangement: list[int]) -> str:
    line_as_list = list(line)
    indexes_of_q = find_all_q(line_as_list)
    for i in arrangement:
        line_as_list[indexes_of_q[i]] = "#"
    return "".join(line_as_list).replace("?", ".")


def to_binary(number: int, num_digits: int) -> str:
    return format(number, '0' + str(num_digits) + 'b')


def count_possible_arrangements(line: str) -> int:
    record, check_values = line.split(" ")
    num_unknowns = sum([c == "?" for c in record])
    num_unplaced_hashs = sum([int(c) for c in check_values.split(",")]) - sum([c == "#" for c in record])
    possible_arrangements = 0
    for c in itertools.combinations(range(0, num_unknowns), num_unplaced_hashs):
        if validate_arrangement(apply_arrangement(line, c)):
            possible_arrangements += 1
    return possible_arrangements


def exercise_1(data: list[str]) -> int:
    return sum(list(map(count_possible_arrangements, data)))


def unfold_record(line: str) -> str:
    factor = 5
    record, check_values = line.split(" ")
    unfolded_record = "?".join([record] * factor)
    unfolded_check_values = ",".join([check_values] * factor)
    return unfolded_record + " " + unfolded_check_values


def exercise_2(data: list[str]) -> int:
    unfolded_data = list(map(unfold_record, data))
    return sum(list(map(count_possible_arrangements, unfolded_data)))
