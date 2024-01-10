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
        outgoing_pulse_type = all(self.input_modules.values())
        return generate_pulses(pulse.destination, self.connected_modules, outgoing_pulse_type)


def exercise_1(data: list[str]) -> int:
    return 0
