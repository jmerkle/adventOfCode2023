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
    return modules.get(pulse.destination).receive_pulse(pulse)


def exercise_1(data: list[str]) -> int:
    return 0
