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

    def __init__(self):
        self.movement_queue = queue.Queue()
        self.already_queued_movements = set()

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


def walk_in_direction(grid: Grid, coords: GridCoordinates, direction: Direction) -> Optional[BeamMovement]:
    line, column = coords
    match direction:
        case Direction.UP:
            line -= 1
        case Direction.RIGHT:
            column += 1
        case Direction.DOWN:
            line += 1
        case Direction.LEFT:
            column -= 1
    if tile_is_on_grid(grid, (line, column)):
        return direction, (line, column)
    return None


def tile_is_on_grid(grid: Grid, coords: GridCoordinates) -> bool:
    line, column = coords
    return all([line >= 0, column >= 0, line < len(grid), column < len(grid[0])])


def calculate_more_movements(grid: Grid, movement: BeamMovement) -> list[BeamMovement]:
    direction, (line, column) = movement
    tile_type = grid[line][column]
    new_directions = calculate_new_directions(tile_type, direction)
    new_movements = [walk_in_direction(grid, (line, column), new_direction) for new_direction in new_directions]
    return list(filter(lambda x: x is not None, new_movements))


def calculate_new_directions(tile_symbol: str, direction: Direction) -> list[Direction]:
    match tile_symbol, direction:
        case ".", _:
            return [direction]

        case "/", Direction.RIGHT:
            return [Direction.UP]
        case "/", Direction.DOWN:
            return [Direction.LEFT]
        case "/", Direction.LEFT:
            return [Direction.DOWN]
        case "/", Direction.UP:
            return [Direction.RIGHT]

        case "\\", Direction.RIGHT:
            return [Direction.DOWN]
        case "\\", Direction.DOWN:
            return [Direction.RIGHT]
        case "\\", Direction.LEFT:
            return [Direction.UP]
        case "\\", Direction.UP:
            return [Direction.LEFT]

        case "-", Direction.RIGHT:
            return [Direction.RIGHT]
        case "-", Direction.DOWN:
            return [Direction.RIGHT, Direction.LEFT]
        case "-", Direction.LEFT:
            return [Direction.LEFT]
        case "-", Direction.UP:
            return [Direction.RIGHT, Direction.LEFT]

        case "|", Direction.RIGHT:
            return [Direction.UP, Direction.DOWN]
        case "|", Direction.DOWN:
            return [Direction.DOWN]
        case "|", Direction.LEFT:
            return [Direction.UP, Direction.DOWN]
        case "|", Direction.UP:
            return [Direction.UP]


def energize(grid: Grid, start_movement: BeamMovement) -> EnergizedGrid:
    energized_grid = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    q = MovementQueue()
    q.put(start_movement)
    next_movement = q.get()
    while next_movement is not None:
        _, (line, column) = next_movement
        energized_grid[line][column] = "#"
        more_movements = calculate_more_movements(grid, next_movement)
        [q.put(mv) for mv in more_movements]
        next_movement = q.get()
    return energized_grid


def count_energized_tiles(grid: EnergizedGrid) -> int:
    return sum([sum([tile == "#" for tile in row]) for row in grid])


def exercise_1(data: Grid) -> int:
    start_movement = (Direction.RIGHT, (0, 0))
    energized_grid = energize(data, start_movement)
    return count_energized_tiles(energized_grid)
