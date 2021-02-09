from curses import color_pair


class Board:
    def __init__(self, width, height, screen):
        self._width = width
        self._height = height
        self._walls = set()
        self._snake = set()
        self._fruits = set()
        self._score = 0
        self._screen = screen

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def set_walls_pos(self, positions):
        self._walls = positions

    def set_snake_pos(self, positions):
        self._snake = positions

    def set_fruits_pos(self, positions):
        self._fruits = positions

    def set_score(self, score):
        self._score = score

    def render(self):
        self._screen.clear()

        for (x, y, symbol, color) in self._walls:
            self._screen.addch(y, x, symbol, color_pair(color.value))

        for (x, y, symbol, color) in self._snake:
            self._screen.addch(y, x, symbol, color_pair(color.value))

        for (x, y, symbol, color) in self._fruits:
            self._screen.addch(y, x, symbol, color_pair(color.value))

        self._screen.addstr(self._height + 1, 0, f"SCORE: {self._score}\n\n")

        self._screen.refresh()
