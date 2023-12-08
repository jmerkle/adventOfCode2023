import numpy as np


def read_file_as_instructions_and_maps(filename: str) -> tuple[str, list[str]]:
    f = open(filename, 'r')
    data = f.read()
    f.close()
    lines = data.split("\n")
    return lines[0], [x for x in lines[1:] if len(x) > 0]


def map_to_triple(map_string: str) -> tuple[str, str, str]:
    return map_string[0:3], map_string[7:10], map_string[12:15]


def maps_as_dictionary(maps_raw: list[str]) -> dict[str, tuple[str, str]]:
    return {position: (left, right) for position, left, right in map(map_to_triple, maps_raw)}


def move(maps: dict[str, tuple[str, str]], location: str, command: str) -> str:
    commands = "LR"
    return maps.get(location)[commands.index(command)]


def exercise_1(data: tuple[str, list[str]]) -> int:
    instructions, maps_raw = data
    location = "AAA"
    destination = "ZZZ"
    steps_taken = 0
    maps: dict[str, tuple[str, str]] = maps_as_dictionary(maps_raw)
    while location != destination:
        location = move(maps, location, instructions[steps_taken % len(instructions)])
        steps_taken += 1
    return steps_taken


def reached_destination(locations: list[str]) -> bool:
    return all(map(lambda location: location.endswith("Z"), locations))


def find_repeating_destinations(maps: dict[str, tuple[str, str]], instructions: str, start_location: str) -> list[tuple[int, int]]:
    visited_positions_at_instruction = [[] for _ in range(len(instructions))]
    visited_positions_at_instruction[0].append((start_location, 0))
    found_destination_positions = []
    location = start_location
    steps_taken = 0
    loop_start = -1
    while loop_start < 0:
        location = move(maps, location, instructions[steps_taken % len(instructions)])
        steps_taken += 1
        if location.endswith("Z"):
            found_destination_positions.append(steps_taken)
        previous_position = [x for x in visited_positions_at_instruction[steps_taken % len(instructions)] if x[0] == location]
        if len(previous_position) > 0:
            loop_start = previous_position[0][1]
        else:
            visited_positions_at_instruction[steps_taken % len(instructions)].append((location, steps_taken))
    # destinations_before_loop = list(filter(lambda p: p < loop_start, found_destination_positions))
    destinations_in_loop = list(filter(lambda p: p >= loop_start, found_destination_positions))
    return list(map(lambda d: (d, steps_taken - loop_start), destinations_in_loop))


def exercise_2(data: tuple[str, list[str]]) -> int:
    instructions, maps_raw = data
    maps: dict[str, tuple[str, str]] = maps_as_dictionary(maps_raw)
    locations: list[str] = list(filter(lambda position: position.endswith("A"), maps.keys()))
    repeating_destinations_for_all_start_locations = list(map(lambda start_location: find_repeating_destinations(maps, instructions, start_location), locations))
    destinations = list(map(lambda d: d[0][0], repeating_destinations_for_all_start_locations))
    return np.lcm.reduce(destinations)
