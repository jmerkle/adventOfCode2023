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


def exercise_2(data: tuple[str, list[str]]) -> int:
    instructions, maps_raw = data
    maps: dict[str, tuple[str, str]] = maps_as_dictionary(maps_raw)
    locations: list[str] = list(filter(lambda position: position.endswith("A"), maps.keys()))
    steps_taken = 0
    while not reached_destination(locations):
        locations = list(map(lambda location: move(maps, location, instructions[steps_taken % len(instructions)]), locations))
        steps_taken += 1
    return steps_taken
