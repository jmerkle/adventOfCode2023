import re


def read_file_as_list_of_lines_and_filter_empty_lines(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x.strip() for x in data.split("\n\n") if len(x) > 0]


def parse_mapping(mapping_as_text):
    lines = mapping_as_text.split("\n")
    if not lines[0].endswith("map:"):
        raise Exception("invalid mapping format: " + mapping_as_text)
    return [extract_numbers(line) for line in lines[1:]]


def extract_numbers(text):
    return [int(n) for n in re.findall(r'\d+', text)]


def find_value_in_mapping(mapping, value):
    matching_row = [row for row in mapping if row[1] <= value < row[1] + row[2]]
    if len(matching_row) > 1:
        raise Exception("more than one row found in mapping" + str(matching_row))
    if len(matching_row) == 0:
        return value
    matching_row = matching_row[0]
    return matching_row[0] + value - matching_row[1]


def value_from_chained_mappings(mappings, value):
    result = value
    for mapping in mappings:
        result = find_value_in_mapping(mapping, result)
    return result


def exercise_1(data):
    return 0
