import numpy as np
from functions import *

data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

matrix = data.split("\n")

parts = []

for line in range(len(matrix)):
    numbers_with_indexes = find_numbers_with_position_indexes(matrix[line])
    for number_with_index in numbers_with_indexes:
        surrounding_symbols = [find_surrounding_symbol_for_entry(matrix, line, column) for column in range(number_with_index[1], number_with_index[2])]
        if True in surrounding_symbols: parts.append(number_with_index[0])

print(parts)
print(sum(parts))

