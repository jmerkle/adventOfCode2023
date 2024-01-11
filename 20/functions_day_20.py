import queue
from abc import ABC, abstractmethod
from enum import Enum


def read_file_as_list_of_lines_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


class Pulse:
    def __init__(self, source: str, destination: str, pulse_type: bool):
        self.source = source
        self.destination = destination
        self.pulse_type = pulse_type

    def __eq__(self, other):
        if not isinstance(other, Pulse):
            return NotImplemented

        return (self.source == other.source
                and self.destination == other.destination
                and self.pulse_type == other.pulse_type)


class Module(ABC):
    @abstractmethod
    def receive_pulse(self, pulse: Pulse) -> list[Pulse]:
        pass


def generate_pulses(source: str, destinations: list[str], pulse_type: bool):
    return list(map(lambda d: Pulse(source, d, pulse_type), destinations))


class FlipFlop:
    def __init__(self, connected_modules: list[str]):
        self.connected_modules = connected_modules
        self.on = False

    def receive_pulse(self, pulse: Pulse) -> list[Pulse]:
        if pulse.pulse_type:
            return []
        self.on = not self.on
        return generate_pulses(pulse.destination, self.connected_modules, self.on)


class Conjunction:
    def __init__(self, input_modules: list[str], connected_modules: list[str]):
        self.input_modules: dict[str, bool] = dict.fromkeys(input_modules, False)
        self.connected_modules = connected_modules

    def receive_pulse(self, pulse: Pulse) -> list[Pulse]:
        self.input_modules.update({pulse.source: pulse.pulse_type})
        outgoing_pulse_type = not all(self.input_modules.values())
        return generate_pulses(pulse.destination, self.connected_modules, outgoing_pulse_type)


def parse_module(module_string: str) -> (str, str, list[str]):
    type_and_name, connected_modules = module_string.split("->")
    connected_modules = list(map(lambda c: c.strip(), connected_modules.split(",")))
    if type_and_name.strip() == "broadcaster":
        return "broadcaster", "broadcaster", connected_modules
    module_type = "flipflop" if type_and_name[0] == "%" else "conjunction"
    name = type_and_name.strip()[1:]
    return module_type, name, connected_modules


def construct_modules_from_input(data: list[str]) -> tuple[dict[str, Module], list[str]]:
    parsed_modules = list(map(parse_module, data))
    modules = {}
    broadcaster = []
    for module_type, name, connected_modules in parsed_modules:
        if module_type == "flipflop":
            modules.update({name: FlipFlop(connected_modules)})
        if module_type == "conjunction":
            input_modules = list(map(lambda m: m[1], filter(lambda m: name in m[2], parsed_modules)))
            modules.update({name: Conjunction(input_modules, connected_modules)})
        if module_type == "broadcaster":
            broadcaster = connected_modules
    return modules, broadcaster


def send_pulse(modules: dict[str, Module], pulse: Pulse) -> list[Pulse]:
    module = modules.get(pulse.destination)
    if module is None:
        return []
    return module.receive_pulse(pulse)


def push_button_and_count(modules: dict[str, Module], broadcaster: list[str]) -> tuple[int, int, bool]:
    pulse_queue = queue.Queue()
    has_rx_been_pinged = False
    broadcast_pulses = map(lambda b: Pulse("broadcaster", b, False), broadcaster)
    [pulse_queue.put(p) for p in broadcast_pulses]
    low_count, high_count = 1, 0  # initialise low with 1 because button push counts as a low pulse
    while pulse_queue.qsize() > 0:
        pulse = pulse_queue.get_nowait()
        if pulse.pulse_type:
            high_count += 1
        else:
            low_count += 1
        has_rx_been_pinged = has_rx_been_pinged or (pulse.destination == "rx" and not pulse.pulse_type)
        new_pulses = send_pulse(modules, pulse)
        [pulse_queue.put(p) for p in new_pulses]
    return low_count, high_count, has_rx_been_pinged


def exercise_1(data: list[str]) -> int:
    modules, broadcaster = construct_modules_from_input(data)
    low_count, high_count = 0, 0
    for _ in range(0, 1000):
        l, h, _ = push_button_and_count(modules, broadcaster)
        low_count += l
        high_count += h
    return low_count*high_count


def exercise_2(data: list[str]) -> int:
    modules, broadcaster = construct_modules_from_input(data)
    push_count = 0
    while not push_button_and_count(modules, broadcaster)[2]:
        push_count += 1
    return push_count + 1
