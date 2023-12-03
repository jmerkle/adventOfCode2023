def cubes_are_valid(available_cubes, shown_cubes):
    colors = list(shown_cubes.keys())
    for c in colors:
        if shown_cubes[c] > available_cubes.get(c, 0):
            return False
    return True
