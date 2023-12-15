from functions_day_15 import *

data_small = read_file_and_split_on_comma('input_small.txt')
data_full = read_file_and_split_on_comma('input.txt')


def test_hash():
    assert hash_function("HASH") == 52
    assert hash_function("rn=1") == 30
    assert hash_function("cm-") == 253


def test_exercise_1():
    assert exercise_1(data_small) == 1320


def test_exercise_1_full_data():
    assert exercise_1(data_full) == 511498


def test_box_and_operation():
    assert box_and_operation("rn=1") == (hash_function("rn"), 1)
    assert box_and_operation("cm-") == (hash_function("cm"), None)
    assert box_and_operation("qp=3") == (hash_function("qp"), 3)
    assert box_and_operation("cm=2") == (hash_function("cm"), 2)
    assert box_and_operation("qp-") == (hash_function("qp"), None)
    assert box_and_operation("pc=4") == (hash_function("pc"), 4)
    assert box_and_operation("ot=9") == (hash_function("ot"), 9)
    assert box_and_operation("ab=5") == (hash_function("ab"), 5)
    assert box_and_operation("pc-") == (hash_function("pc"), None)
    assert box_and_operation("pc=6") == (hash_function("pc"), 6)
    assert box_and_operation("ot=7") == (hash_function("ot"), 7)


def test_add_to_empty_box():
    box = []
    box = add_to_box(box, ("rn", 1))
    assert box == [("rn", 1)]


def test_add_to_non_empty_box():
    box = [("rn", 1)]
    box = add_to_box(box, ("ab", 1))
    assert box == [("rn", 1), ("ab", 1)]


def test_replace_in_box():
    box = [("rn", 1)]
    box = add_to_box(box, ("rn", 2))
    assert box == [("rn", 2)]


def test_remove_from_box():
    box = [("ab", 1), ("rn", 1), ("cd", 1)]
    box = remove_from_box(box, "rn")
    assert box == [("ab", 1), ("cd", 1)]


def test_exercise_2():
    assert exercise_2(data_small) == 145
