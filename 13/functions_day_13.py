def read_file_as_list_of_sections(filename: str) -> list[list[str]]:
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x.strip().split("\n") for x in data.split("\n\n") if len(x) > 0]


def exercise_1(data: list[list[str]]) -> int:
    return 0
