import numpy as np


def surrounding_symbols_of_numerical_values(data):
    matrix = data.split("\n")
    result = np.full([len(matrix), len(matrix[0])], False)
    for line in range(len(matrix)):
        for column in range(len(matrix[0])):
            result[line][column] = find_surrounding_symbol_for_entry(matrix, line, column)
    return result


def find_surrounding_symbol_for_entry(matrix, line, column):
    max_line = len(matrix) - 1
    max_column = len(matrix[0]) - 1
    values = []
    # above left
    if line > 0 and column > 0: values.append(matrix[line - 1][column - 1])
    # above
    if line > 0: values.append(matrix[line - 1][column])
    # above right
    if line > 0 and column < max_column: values.append(matrix[line - 1][column + 1])
    # left
    if column > 0: values.append(matrix[line][column - 1])
    # right
    if column < max_column: values.append(matrix[line][column + 1])
    # below_left
    if line < max_line and column > 0: values.append(matrix[line + 1][column - 1])
    # below
    if line < max_line: values.append(matrix[line + 1][column])
    # below right
    if line < max_line and column < max_column: values.append(matrix[line + 1][column + 1])
    for char in values:
        if is_symbol(char):
            return True
    return False


def is_symbol(char):
    return not char.isnumeric() and not char == "."
