import curses
from enum import Enum


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    RIGHT = (1, 0)
    LEFT = (-1, 0)

    @classmethod
    def from_key(cls, key):
        if key == curses.KEY_UP:
            return cls.UP
        elif key == curses.KEY_DOWN:
            return cls.DOWN
        elif key == curses.KEY_LEFT:
            return cls.LEFT
        elif key == curses.KEY_RIGHT:
            return cls.RIGHT
        else:
            return None

    @classmethod
    def is_opposite(cls, dir_1, dir_2):
        return (
            dir_1 == cls.UP
            and dir_2 == cls.DOWN
            or dir_1 == cls.DOWN
            and dir_2 == cls.UP
            or dir_1 == cls.RIGHT
            and dir_2 == cls.LEFT
            or dir_1 == cls.LEFT
            and dir_2 == cls.RIGHT
        )
