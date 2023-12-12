from functions_day_12 import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')


def test_find_arrangements():
    assert count_possible_arrangements("?.?????#???#? 1,1,2,2") == 22
    assert count_possible_arrangements("#???#?? 1") == 0

    assert count_possible_arrangements("??# 1") == 1
    assert count_possible_arrangements("???.### 1,1,3") == 1
    assert count_possible_arrangements(".??..??...?##. 1,1,3") == 4
    assert count_possible_arrangements("?#?#?#?#?#?#?#? 1,3,1,6") == 1
    assert count_possible_arrangements("????.#...#... 4,1,1") == 1
    assert count_possible_arrangements("????.######..#####. 1,6,5") == 4
    assert count_possible_arrangements("?###???????? 3,2,1") == 10
    assert count_possible_arrangements("????.#????#?????#??# 1,2,1,1,7") == 5


def test_unfold_record():
    assert unfold_record(".# 1") == ".#?.#?.#?.#?.# 1,1,1,1,1"


def test_find_arrangements_unfolded():
    assert count_possible_arrangements(unfold_record("?.?????#???#? 1,1,2,2")) == 1
    assert count_possible_arrangements(unfold_record("???.### 1,1,3")) == 1
    assert count_possible_arrangements(unfold_record(".??..??...?##. 1,1,3")) == 16384
    assert count_possible_arrangements(unfold_record("?#?#?#?#?#?#?#? 1,3,1,6")) == 1
    assert count_possible_arrangements(unfold_record("????.#...#... 4,1,1")) == 16
    assert count_possible_arrangements(unfold_record("????.######..#####. 1,6,5")) == 2500
    assert count_possible_arrangements(unfold_record("?###???????? 3,2,1")) == 506250


def test_record_could_start_with():
    assert record_could_start_with("????.", 1)
    assert record_could_start_with("??.", 1)
    assert record_could_start_with("??.", 2)
    assert not record_could_start_with("?#", 1)
    assert not record_could_start_with("??#", 2)
    assert not record_could_start_with("?.", 2)


def test_generate_possible_remaining_records():
    assert generate_possible_remaining_records("#", 1) == [""]
    assert generate_possible_remaining_records(".", 1) == []
    assert generate_possible_remaining_records("??#", 1) == ["#", ""]
    assert generate_possible_remaining_records("???#?????#??#", 1) == ["?#?????#??#", "#?????#??#", "????#??#"]
    assert generate_possible_remaining_records("?#?#?#?#?#?#?#?", 1) == ["#?#?#?#?#?#?"]
    assert generate_possible_remaining_records("?#?#?#?#?#?#?#?", 2) == ["#?#?#?#?#?#?"]
    assert generate_possible_remaining_records("?#?#?#?#?#?#?#?", 3) == ["#?#?#?#?#?"]


def test_exercise_1():
    assert exercise_1(data_small) == 21


def test_exercise_1_full_data():
    assert exercise_1(data_full) == 7771


def test_exercise_2():
    assert exercise_2(data_small) == 525152


def test_exercise_2_full_data():
    assert exercise_2(data_full) == 525152
