from functools import reduce


def parse_game(game):
    if not game.startswith("Game"):
        return {}
    [game_id, rounds] = game.split(":")
    game_num = int(game_id.split()[1])
    parsed_rounds = map(lambda round: parse_round(round), rounds.split(";"))
    parsed_rounds = reduce(lambda r1, r2: merge_rounds(r1, r2), parsed_rounds)
    return [game_num, parsed_rounds]


def parse_round(round):
    dice = round.split(",")
    parsed_dice = map(lambda die: parse_die_color(die), dice)
    return reduce((lambda d1, d2: d1 | d2), parsed_dice)


def parse_die_color(die_color):
    [amount, color] = die_color.strip().split()
    return {
        color: int(amount)
    }


def merge_rounds(round1, round2):
    keys = set(list(round1.keys()) + list(round2.keys()))
    merged = {}
    for k in keys:
        merged[k] = max(round1.get(k, 0), round2.get(k, 0))

    return merged
