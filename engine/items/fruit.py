from abc import ABC

from display.color import Color


class Fruit(ABC):
    def __init__(self, value, pos, symbol, color):
        self._value = value
        self._pos = pos
        self._symbol = symbol
        self._color = color
        self._active = True

    @property
    def value(self):
        return self._value

    @property
    def pos(self):
        return self._pos

    @property
    def symbol(self):
        return self._symbol

    @property
    def color(self):
        return self._color

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value

    def render(self):
        (x, y) = self._pos
        return x, y, self._symbol, self._color


class Apple(Fruit):
    APPLE_SYMBOL = "o"
    APPLE_VALUE = 1
    APPLE_COLOR = Color.APPLE

    def __init__(self, pos):
        super(Apple, self).__init__(
            Apple.APPLE_VALUE, pos, Apple.APPLE_SYMBOL, Apple.APPLE_COLOR
        )
