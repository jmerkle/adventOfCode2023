from functions_day_20 import *

data_small_1 = read_file_as_list_of_lines_and_filter_empty_lines('input_small_1.txt')
data_small_2 = read_file_as_list_of_lines_and_filter_empty_lines('input_small_2.txt')
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

    assert output_1 == [Pulse("m", "out", True)]
    assert output_2 == [Pulse("m", "out", True)]
    assert output_3 == [Pulse("m", "out", False)]
    assert output_4 == [Pulse("m", "out", False)]
    assert output_5 == [Pulse("m", "out", True)]


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


def test_send_single_pulse():
    data = [
        "broadcaster -> a, b, c",
        "%a -> b",
        "%b -> c",
        "%c -> inv",
        "&inv -> a"
    ]
    modules, _ = construct_modules_from_input(data)
    # broadcast
    assert (send_pulse(modules, Pulse("broadcaster", "a", False))
            == [Pulse("a", "b", True)])
    assert (send_pulse(modules, Pulse("broadcaster", "b", False))
            == [Pulse("b", "c", True)])
    assert (send_pulse(modules, Pulse("broadcaster", "c", False))
            == [Pulse("c", "inv", True)])
    # generated pulses
    assert (send_pulse(modules, Pulse("a", "b", True))
            == [])
    assert (send_pulse(modules, Pulse("b", "c", True))
            == [])
    assert (send_pulse(modules, Pulse("c", "inv", True))
            == [Pulse("inv", "a", False)])
    assert (send_pulse(modules, Pulse("inv", "a", False))
            == [Pulse("a", "b", False)])
    assert (send_pulse(modules, Pulse("a", "b", False))
            == [Pulse("b", "c", False)])
    assert (send_pulse(modules, Pulse("b", "c", False))
            == [Pulse("c", "inv", False)])
    assert (send_pulse(modules, Pulse("c", "inv", False))
            == [Pulse("inv", "a", True)])
    assert (send_pulse(modules, Pulse("inv", "a", True))
            == [])


def test_push_button_and_count():
    data = [
        "broadcaster -> a, b, c",
        "%a -> b",
        "%b -> c",
        "%c -> inv",
        "&inv -> a"
    ]
    modules, broadcaster = construct_modules_from_input(data)
    low, high, _ = push_button_and_count(modules, broadcaster)
    assert low == 8
    assert high == 4


def test_exercise_1():
    assert exercise_1(data_small_1) == 32000000
    assert exercise_1(data_small_2) == 11687500


def test_exercise_1_full():
    assert exercise_1(data_full) == 886701120


def test_exercise_2():
    assert exercise_2(data_full) == 228134431501037
