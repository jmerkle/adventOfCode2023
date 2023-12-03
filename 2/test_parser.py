from game_parser import *

def test_parse_die_color():
    color = "3 blue"
    parsed = parse_die_color(color)
    assert parsed == {
        "blue": 3
    }

def test_parse_round():
    color = "3 blue, 4 red"
    parsed = parse_round(color)
    assert parsed == {
        "blue": 3,
        "red": 4
    }

def test_merge_rounds():
    r1 = {
        "blue": 3,
        "red": 4
    }
    r2 = {
        "blue": 5,
        "green": 4
    }

    merged = merge_rounds(r1, r2)
    assert merged["blue"] == 5
    assert merged["green"] == 4
    assert merged["red"] == 4

def test_parse_game():
    game = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game_num, parsed = parse_game(game)
    assert parsed["blue"] == 6
    assert parsed["red"] == 4
    assert parsed["green"] == 2
    assert game_num == 1

def test_fail_on_invalid_line():
    game = ""
    parsed = parse_game(game)
    assert parsed == {}
