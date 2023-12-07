from functions_day_7 import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')


def test_hand_type():
    assert hand_type("23456") == 0
    assert hand_type("A23A4") == 1
    assert hand_type("23432") == 2
    assert hand_type("TTT98") == 3
    assert hand_type("23332") == 4
    assert hand_type("AA8AA") == 5
    assert hand_type("AAAAA") == 6


def test_rank_hands():
    hands_ranked = sorted(data_small, key=enumerate_hand)
    assert hands_ranked[0] == "32T3K 765"
    assert hands_ranked[1] == "KTJJT 220"
    assert hands_ranked[2] == "KK677 28"
    assert hands_ranked[3] == "T55J5 684"
    assert hands_ranked[4] == "QQQJA 483"


def test_exercise_1():
    assert exercise_1(data_small) == 6440


def test_exercise_1_all_data():
    assert exercise_1(data_full) == 247823654


def test_hand_type_with_joker():
    assert hand_type_with_joker("23456") == 0
    assert hand_type_with_joker("A23A4") == 1
    assert hand_type_with_joker("23432") == 2
    assert hand_type_with_joker("TTT98") == 3
    assert hand_type_with_joker("23332") == 4
    assert hand_type_with_joker("AA8AA") == 5
    assert hand_type_with_joker("AAAAA") == 6

    assert hand_type_with_joker("32T3K") == 1
    assert hand_type_with_joker("KK677") == 2
    assert hand_type_with_joker("T55J5") == 5
    assert hand_type_with_joker("KTJJT") == 5
    assert hand_type_with_joker("QQQJA") == 5


def test_exercise_2():
    assert exercise_2(data_small) == 5905


def test_exercise_2_all_data():
    assert exercise_2(data_full) == 245461700
