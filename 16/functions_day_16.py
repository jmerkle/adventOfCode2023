import queue
from enum import Enum
from typing import TypeAlias, Optional


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


GridCoordinates: TypeAlias = tuple[int, int]
Grid: TypeAlias = list[list[str]]
EnergizedGrid: TypeAlias = list[list[str]]
BeamMovement: TypeAlias = tuple[Direction, GridCoordinates]


class MovementQueue:
    movement_queue = queue.Queue()
    already_queued_movements = set()

    def put(self, movement: BeamMovement) -> None:
        if movement not in self.already_queued_movements:
            self.movement_queue.put(movement)
            self.already_queued_movements.add(movement)

    def get(self) -> Optional[BeamMovement]:
        try:
            return self.movement_queue.get_nowait()
        except queue.Empty:
            return None


def read_file_as_list_of_list_and_filter_empty_lines(filename: str) -> Grid:
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return [list(x) for x in data.split("\n") if len(x) > 0]


def energize(grid: Grid, start_movement: BeamMovement) -> EnergizedGrid:


    return []


def count_energized_tiles(grid: EnergizedGrid) -> int:
    return 0


def exercise_1(data: Grid) -> int:
    start_movement = (Direction.RIGHT, (0, 0))
    energized_grid = energize(data, start_movement)
    return count_energized_tiles(energized_grid)
