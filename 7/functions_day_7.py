
def read_file_as_list_of_lines_and_filter_empty_lines(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


def exercise_1(data):
    return 0
