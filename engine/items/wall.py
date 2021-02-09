from abc import ABC

from display.color import Color


class Wall(ABC):
    def __init__(self, pos, symbol, color):
        self._pos = pos
        self._symbol = symbol
        self._color = color

    @property
    def pos(self):
        return self._pos

    @property
    def symbol(self):
        return self._symbol

    @property
    def color(self):
        return self._color

    def render(self):
        (x, y) = self._pos
        return x, y, self._symbol, self._color


class VerticalWall(Wall):
    V_WALL_SYMBOL = "|"
    V_WALL_COLOR = Color.WALL

    def __init__(self, pos):
        super(VerticalWall, self).__init__(
            pos, VerticalWall.V_WALL_SYMBOL, VerticalWall.V_WALL_COLOR
        )


class HorizontalWall(Wall):
    H_WALL_SYMBOL = "="
    H_WALL_COLOR = Color.WALL

    def __init__(self, pos):
        super(HorizontalWall, self).__init__(
            pos, HorizontalWall.H_WALL_SYMBOL, HorizontalWall.H_WALL_COLOR
        )
