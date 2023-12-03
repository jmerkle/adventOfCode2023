from game_parser import parse_game

f = open('input.txt', 'r')
data = f.read()
f.close()
lines = data.split('\n')

all_cubes = {
    "blue": 14,
    "green": 13,
    "red": 12
}

for line in lines:
    print("##########")
    print(line)
    print(parse_game(line))
