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


def test_conjunction():
    module = Conjunction(["in1", "in2"], ["out"])
    output_1 = module.receive_pulse(Pulse("in1", "m", True))
    output_2 = module.receive_pulse(Pulse("in2", "m", False))
    output_3 = module.receive_pulse(Pulse("in2", "m", True))
    output_4 = module.receive_pulse(Pulse("in1", "m", True))
    output_5 = module.receive_pulse(Pulse("in1", "m", False))

    assert output_1 == [Pulse("m", "out", False)]
    assert output_2 == [Pulse("m", "out", False)]
    assert output_3 == [Pulse("m", "out", True)]
    assert output_4 == [Pulse("m", "out", True)]
    assert output_5 == [Pulse("m", "out", False)]


def test_construct_modules_from_input():
    data = [
        "broadcaster -> a, b, c",
        "%a -> b",
        "%b -> c",
        "%c -> inv",
        "&inv -> a"
    ]
    modules, broadcaster = construct_modules_from_input(data)
    assert broadcaster == ["a", "b", "c"]
    a = modules.get("a")
    assert isinstance(a, FlipFlop)
    assert a.__getattribute__("connected_modules") == ["b"]

    b = modules.get("b")
    assert isinstance(b, FlipFlop)
    assert b.__getattribute__("connected_modules") == ["c"]

    c = modules.get("c")
    assert isinstance(c, FlipFlop)
    assert c.__getattribute__("connected_modules") == ["inv"]

    inv = modules.get("inv")
    assert isinstance(inv, Conjunction)
    assert inv.__getattribute__("connected_modules") == ["a"]
    assert inv.__getattribute__("input_modules") == {"c": False}


def test_exercise_1():
    assert exercise_1(data_small) == 32000000
