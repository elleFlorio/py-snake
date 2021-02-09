from collections import deque


class Snake:
    def __init__(self, body, symbol, color):
        self._body = deque(body)
        self._symbol = symbol
        self._color = color
        self._bonus = 0

    def move(self, direction):
        head = self._body[-1]

        self._body.append(tuple(sum(x) for x in zip(head, direction.value)))
        if self._bonus > 0:
            self._bonus -= 1
        else:
            self._body.popleft()

    def add_bonus(self, bonus):
        self._bonus += bonus

    def render(self):
        return list(map(lambda t: (t[0], t[1], self._symbol, self._color), self._body))

    @property
    def head(self):
        return self._body[-1]

    @property
    def body(self):
        return list(self._body)[:-1]
