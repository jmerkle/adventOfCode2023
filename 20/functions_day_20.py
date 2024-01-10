from abc import ABC, abstractmethod
from enum import Enum


def read_file_as_list_of_lines_and_filter_empty_lines(filename: str):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [x for x in data.split("\n") if len(x) > 0]


class PulseType(Enum):
    HIGH = "H"
    LOW = "L"


class Pulse:
    def __init__(self, source: str, destination: str, type: PulseType):
        self.source = source
        self.destination = destination
        self.type = PulseType


class Module(ABC):
    @abstractmethod
    def receive_pulse(self, pulse: Pulse) -> list[Pulse]:
        pass


class FlipFlop:
    def __init__(self, connected_modules: list[str]):
        self.connected_modules = connected_modules
        self.on = False

    def receive_pulse(self, pulse: Pulse) -> list[Pulse]:
        return []


class Conjunction:
    def __init__(self, input_modules: list[str], connected_modules: list[str]):
        self.input_modules = input_modules
        self.connected_modules = connected_modules

    def receive_pulse(self, pulse: Pulse) -> list[Pulse]:
        return []


def exercise_1(data: list[str]) -> int:
    return 0
