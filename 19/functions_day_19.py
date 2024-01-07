def read_file_as_list_of_sections(filename: str) -> list[list[str]]:
    f = open(filename, 'r')
    data = f.read()
    f.close()
    sections = [x.strip() for x in data.split("\n\n") if len(x) > 0]
    return [x.split("\n") for x in sections if len(x) > 0]


def exercise_1(data: list[list[str]]) -> int:
    return 0
