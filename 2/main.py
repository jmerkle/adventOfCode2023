from game_parser import parse_game
from process_cubes import *

f = open('input.txt', 'r')
data = f.read()
f.close()
lines = data.split('\n')

all_cubes = {
    "blue": 14,
    "green": 13,
    "red": 12
}

sum_of_ids = 0
sum_of_power = 0

for line in lines:
    if line.startswith("Game"):
        print("##########")
        print(line)
        [game_id, parsed] = parse_game(line)
        print(parsed)
        valid = cubes_are_valid(all_cubes, parsed)
        print(valid)
        if valid:
            sum_of_ids += game_id
        power = power_of_cubes(parsed)
        print(power)
        sum_of_power += power

print("sum of valid ids:")
print(sum_of_ids)
print("sum of power:")
print(sum_of_power)
