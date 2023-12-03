def cubes_are_valid(available_cubes, shown_cubes):
    colors = list(shown_cubes.keys())
    for c in colors:
        if shown_cubes[c] > available_cubes.get(c, 0):
            return False
    return True


def power_of_cubes(cubes):
    values = list(cubes.values())
    power = 1
    for v in values:
        power = power * v
    return power
