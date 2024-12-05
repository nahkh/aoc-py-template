from __future__ import annotations
from dataclasses import dataclass
from typing import Generator
from enum import Enum


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        elif isinstance(other, Direction):
            return self + other.as_position()
        else:
            raise ValueError(f'Position {self} cannot be added with {other} as it is of type {type(other)}')

    def __sub__(self, other):
        if isinstance(other, Position):
            return Position(self.x - other.x, self.y - other.y)
        elif isinstance(other, Direction):
            return self - other.as_position()
        else:
            raise ValueError(f'Position {self} cannot be subtracted with {other} as it is of type {type(other)}')

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def direct_neighbors(self) -> Generator[Position]:
        for direction in Direction.direct():
            yield self + direction.as_position()

    def diagonal_neighbors(self) -> Generator[Position]:
        for direction in Direction.diagonal():
            yield self + direction.as_position()

    def all_neighbors(self) -> Generator[Position]:
        for direction in Direction.all():
            yield self + direction.as_position()


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UP_LEFT = 5
    UP_RIGHT = 6
    DOWN_LEFT = 7
    DOWN_RIGHT = 8

    @classmethod
    def all(cls) -> Generator[Direction]:
        yield Direction.UP
        yield Direction.DOWN
        yield Direction.LEFT
        yield Direction.RIGHT
        yield Direction.UP_LEFT
        yield Direction.UP_RIGHT
        yield Direction.DOWN_LEFT
        yield Direction.DOWN_RIGHT

    @classmethod
    def direct(cls) -> Generator[Direction]:
        yield Direction.UP
        yield Direction.DOWN
        yield Direction.LEFT
        yield Direction.RIGHT

    @classmethod
    def diagonal(cls) -> Generator[Direction]:
        yield Direction.UP_LEFT
        yield Direction.UP_RIGHT
        yield Direction.DOWN_LEFT
        yield Direction.DOWN_RIGHT

    def as_position(self) -> Position:
        return _DIRECTION_TO_POSITION[self]

    def reverse(self) -> Direction:
        return _REVERSE_DIRECTION[self]

    def rot90(self) -> Direction:
        return _ROT90_DIRECTION[self]


_DIRECTION_TO_POSITION = {
    Direction.UP: Position(0, -1),
    Direction.DOWN: Position(0, 1),
    Direction.LEFT: Position(-1, 0),
    Direction.RIGHT: Position(1, 0),
    Direction.UP_LEFT: Position(-1, -1),
    Direction.UP_RIGHT: Position(1, -1),
    Direction.DOWN_LEFT: Position(-1, 1),
    Direction.DOWN_RIGHT: Position(1, 1),
}

_REVERSE_DIRECTION = {
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.LEFT: Direction.RIGHT,
    Direction.RIGHT: Direction.LEFT,
    Direction.UP_LEFT: Direction.DOWN_RIGHT,
    Direction.UP_RIGHT: Direction.DOWN_LEFT,
    Direction.DOWN_LEFT: Direction.UP_RIGHT,
    Direction.DOWN_RIGHT: Direction.UP_LEFT,
}

_ROT90_DIRECTION = {
    Direction.UP: Direction.LEFT,
    Direction.DOWN: Direction.RIGHT,
    Direction.LEFT: Direction.DOWN,
    Direction.RIGHT: Direction.UP,
    Direction.UP_LEFT: Direction.DOWN_LEFT,
    Direction.UP_RIGHT: Direction.UP_LEFT,
    Direction.DOWN_LEFT: Direction.DOWN_RIGHT,
    Direction.DOWN_RIGHT: Direction.UP_RIGHT,
}
