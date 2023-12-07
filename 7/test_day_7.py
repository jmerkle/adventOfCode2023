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


def test_enumerate_hand():
    assert enumerate_hand("32T3K 765") < enumerate_hand("KTJJT 220")
    assert enumerate_hand("KTJJT 220") < enumerate_hand("KK677 28")
    assert enumerate_hand("KK677 28") < enumerate_hand("T55J5 684")
    assert enumerate_hand("T55J5 684") < enumerate_hand("QQQJA 483")


def test_rank_hands():
    hands_ranked = rank_hands(data_small)
    assert hands_ranked[0] == "32T3K 765"
    assert hands_ranked[1] == "KTJJT 220"
    assert hands_ranked[2] == "KK677 28"
    assert hands_ranked[3] == "T55J5 684"
    assert hands_ranked[4] == "QQQJA 483"


def test_exercise_1():
    assert exercise_1(data_small) == 6440


def test_exercise_1_all_data():
    print(exercise_1(data_full))
