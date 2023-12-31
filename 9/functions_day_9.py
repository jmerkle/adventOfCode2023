def read_file_as_list_of_lines_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


def derive_line(line: list[int]) -> list[int]:
    if len(line) > 1:
        return [line[1] - line[0]] + derive_line(line[1:])
    return []


def derive_all_line(line: list[int]) -> list[list[int]]:
    if any(x != 0 for x in line):
        return [line] + derive_all_line(derive_line(line))
    return [line]


def _extrapolate(derived_reversed: list[list[int]], backwards: bool) -> list[list[int]]:
    if all(x == 0 for x in derived_reversed[0]):
        expanded_line = derived_reversed[0] + [0]
        if len(derived_reversed) < 2:
            return [expanded_line]
    else:
        expanded_line = derived_reversed[0]
    if backwards:
        next_line = [derived_reversed[1][0] - expanded_line[0]] + derived_reversed[1]
    else:
        next_line = derived_reversed[1] + [derived_reversed[1][-1] + expanded_line[-1]]
    if len(derived_reversed) > 2:
        return [expanded_line] + _extrapolate([next_line] + derived_reversed[2:], backwards)
    return [expanded_line, next_line]


def extrapolate(derived_all: list[list[int]], backwards: bool = False) -> list[list[int]]:
    return list(reversed(_extrapolate(list(reversed(derived_all)), backwards)))


def process_line(line: str, backwards: bool = False) -> int:
    line_as_number = list(map(lambda c: int(c), line.split(" ")))
    derive_all = derive_all_line(line_as_number)
    extrapolated = extrapolate(derive_all, backwards)
    if backwards:
        return extrapolated[0][0]
    else:
        return extrapolated[0][-1]


def exercise_1(data: list[str]) -> int:
    return sum(map(lambda line: process_line(line), data))


def exercise_2(data: list[str]) -> int:
    return sum(map(lambda line: process_line(line, True), data))
