from functions import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')


def test_read_file():
    data = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
    assert data[0] == "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert data[-1] == "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"


def test_parse_card():
    card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    [winning_numbers, card_numbers] = parse_card(card)
    assert winning_numbers == [41, 48, 83, 86, 17]
    assert card_numbers == [83, 86, 6, 31, 17, 9, 48, 53]


def test_calculate_points_for_card():
    card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert calculate_points_for_card(card) == 8


def test_calculate_points_for_losing_card():
    card = "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36"
    assert calculate_points_for_card(card) == 0


def test_exercise_1():
    assert exercise_1(data_small) == 13


def test_exercise_1_full_data():
    data = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')
    print(exercise_1(data))


def test_calculate_wins_for_all_card():
    assert calculate_wins_for_all_cards(data_small) == [4, 2, 2, 1, 0, 0]


def test_exercise_2():
    assert exercise_2(data_small) == 30


def test_exercise_2_full_data():
    data = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')
    print(exercise_2(data))
