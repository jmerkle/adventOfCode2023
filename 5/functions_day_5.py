import re
import sys


def read_file_as_list_of_sections(filename):
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
    seeds = extract_numbers(data[0].split(":")[1])
    mappings = [parse_mapping(line) for line in data[1:]]
    locations = [value_from_chained_mappings(mappings, seed) for seed in seeds]
    return min(locations)


def exercise_2(data):
    seed_ranges = chunk_list_into_pairs(extract_numbers(data[0].split(":")[1]))
    seeds = flatten_list_and_remove_duplicates([expand_seed_range(seed_range) for seed_range in seed_ranges])
    mappings = [parse_mapping(line) for line in data[1:]]
    locations = [value_from_chained_mappings(mappings, seed) for seed in seeds]
    return min(locations)


def exercise_2_improved(data):
    min_location = sys.maxsize
    mappings = [parse_mapping(line) for line in data[1:]]
    seed_ranges = chunk_list_into_pairs(extract_numbers(data[0].split(":")[1]))
    for seed_range in seed_ranges:
        print("processing seed range ", seed_range)
        seeds = expand_seed_range(seed_range)
        print(" with ", len(seeds), " values")
        min_location = min(min_location, process_seed_batch(mappings, seeds))
    return min_location


def process_seed_batch(mappings, seeds):
    min_location = sys.maxsize
    for seed in seeds:
        min_location = min(min_location, value_from_chained_mappings(mappings, seed))
    return min_location


def chunk_list_into_pairs(li):
    for i in range(0, len(li), 2):
        yield li[i:i + 2]


def expand_seed_range(seed_range):
    return [v for v in range(seed_range[0], seed_range[0] + seed_range[1])]


def flatten_list_and_remove_duplicates(list_of_lists):
    return list(dict.fromkeys([item for sub_list in list_of_lists for item in sub_list]))
