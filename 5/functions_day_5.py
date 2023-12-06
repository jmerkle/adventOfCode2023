import re
import sys
import time
import multiprocessing as mp
import math

from functools import partial


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
    return chunk_list(li, 2)


def chunk_list(li, chunk_size):
    return [li[i: i + chunk_size] for i in range(0, len(li), chunk_size)]


def expand_seed_range(seed_range):
    return [v for v in range(seed_range[0], seed_range[0] + seed_range[1])]


def flatten_list_and_remove_duplicates(list_of_lists):
    return list(dict.fromkeys([item for sub_list in list_of_lists for item in sub_list]))


def process_range(mappings, seed_range):
    [range_start, range_size] = seed_range
    location_start = value_from_chained_mappings(mappings, range_start)
    if range_size < 2:
        return location_start
    location_end = value_from_chained_mappings(mappings, seed_range[0] + range_size - 1)
    if location_end - location_start + 1 == range_size:
        return location_start
    split = math.floor(range_size / 2)
    print("splitting on ", split)
    return min(
        process_range(mappings, [range_start, split]),
        process_range(mappings, [range_start + split, math.ceil(range_size / 2)])
    )

def exercise_2_ranges(data):
    start_time = time.time()
    min_location = sys.maxsize
    mappings = [parse_mapping(line) for line in data[1:]]
    seed_ranges = chunk_list_into_pairs(extract_numbers(data[0].split(":")[1]))
    range_cnt = 0
    for seed_range in seed_ranges:
        range_cnt += 1
        print("processing seed range ", range_cnt, "/", len(seed_ranges), ": ", seed_range)
        min_location = min(min_location, process_range(mappings, seed_range))
    end_time = time.time()
    print("all finished after ", end_time - start_time, " seconds")
    print("min is ", min_location)
    return min_location


def exercise_2_parallel(data, chunk_size):
    start_time = time.time()
    min_location = sys.maxsize
    mappings = [parse_mapping(line) for line in data[1:]]
    mapping_fun = partial(process_seed_batch, mappings)
    seed_ranges = chunk_list_into_pairs(extract_numbers(data[0].split(":")[1]))
    pool = mp.Pool(mp.cpu_count())
    print(pool)
    range_cnt = 0
    for seed_range in seed_ranges:
        range_cnt += 1
        print("processing seed range ", range_cnt, "/", len(seed_ranges), ": ", seed_range)
        seeds = expand_seed_range(seed_range)
        print(" with ", len(seeds), " values")
        chunked_seeds = list(chunk_list(seeds, chunk_size))
        tmp_result = pool.map(mapping_fun, chunked_seeds)
        min_location = min(min_location, min(tmp_result))
        interim_time = time.time()
        print("range finished after ", interim_time - start_time, " seconds")
    end_time = time.time()
    pool.close()
    print("all finished after ", end_time - start_time, " seconds")
    print("min is ", min_location)
    return min_location
