from functions_day_20 import *

data_small = read_file_as_list_of_lines_and_filter_empty_lines('input_small.txt')
data_full = read_file_as_list_of_lines_and_filter_empty_lines('input.txt')


def test_flip_flip():
    module = FlipFlop(["a", "b"])
    output_high_1 = module.receive_pulse(Pulse("s", "m", True))
    output_low_1 = module.receive_pulse(Pulse("s", "m", False))
    output_high_2 = module.receive_pulse(Pulse("s", "m", True))
    output_low_2 = module.receive_pulse(Pulse("s", "m", False))
    output_low_3 = module.receive_pulse(Pulse("s", "m", False))

    assert output_high_1 == []
    assert output_high_2 == []
    assert output_low_1 == [Pulse("m", "a", True), Pulse("m", "b", True)]
    assert output_low_2 == [Pulse("m", "a", False), Pulse("m", "b", False)]
    assert output_low_3 == [Pulse("m", "a", True), Pulse("m", "b", True)]


def test_exercise_1():
    assert exercise_1(data_small) == 32000000
