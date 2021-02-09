class Player:
    def __init__(self, name, symbol, color, screen):
        self._name = name
        self._score = 0
        self._screen = screen
        self._symbol = symbol
        self._color = color

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def color(self):
        return self._color

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def get_input(self):
        return self._screen.getch()
