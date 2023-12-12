import re

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


def apply_arrangement(line: str, arrangement: str) -> str:
    for i in arrangement:
        if i=="1":
            line = line.replace("?", "#", 1)
        else:
            line = line.replace("?", ".", 1)
    return line


def to_binary(number: int, num_digits: int) -> str:
    return format(number, '0'+str(num_digits)+'b')


def count_possible_arrangements(line: str) -> int:
    num_unknowns = sum([c == "?" for c in line])
    possible_arrangements = 0
    for i in range(0, 2**num_unknowns):
        if validate_arrangement(apply_arrangement(line, to_binary(i, num_unknowns))):
            possible_arrangements += 1
    return possible_arrangements

def exercise_1(data: list[str]) -> int:
    return sum(list(map(count_possible_arrangements, data)))
