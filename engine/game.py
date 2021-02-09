import time
from random import randint

from .items.direction import Direction
from .items.snake import Snake
from .items.fruit import Apple
from .items.wall import VerticalWall, HorizontalWall
from display.board import Board


class Game:
    def __init__(self, player, screen):
        self._player = player
        self._board = Board(24, 10, screen)
        self._snake = Snake([(2, 5), (3, 5), (4, 5)], player.symbol, player.color)
        self._fruits = set()
        self._eaten_fruits = set()
        self._walls = set()
        self._score = 0
        self._direction = Direction.RIGHT
        self._game_over = False

        self._add_fruit()

        for w in range(1, self._board.width - 1):
            self._walls.add(HorizontalWall((w, 0)))
            self._walls.add(HorizontalWall((w, self._board.height - 1)))

        for h in range(self._board.height):
            self._walls.add(VerticalWall((0, h)))
            self._walls.add(VerticalWall((self._board.width - 1, h)))

        walls_pos = list(map(lambda wall: wall.render(), self._walls))
        self._board.set_walls_pos(walls_pos)

    def _check_fruits(self, pos):
        for fruit in self._fruits:
            if pos == fruit.pos:
                bonus = fruit.value
                self._eaten_fruits.add(fruit)
                self._add_fruit()
                return bonus

        return 0

    def _clean_fruits(self):
        for fruit in self._eaten_fruits:
            self._fruits.remove(fruit)

        self._eaten_fruits.clear()

    def _check_collision(self, pos):
        for w in self._walls:
            if w.pos == pos:
                return True

        for s in self._snake.body:
            if s == pos:
                return True

        return False

    def _add_fruit(self):
        occupied = set(list(self._snake.body))
        occupied.add(self._snake.head)
        new_fruit_pos = (
            randint(1, self._board.width - 2),
            randint(1, self._board.height - 2),
        )
        while new_fruit_pos in occupied:
            new_fruit_pos = (
                randint(1, self._board.width - 2),
                randint(1, self._board.height - 2),
            )

        self._fruits.add(Apple(new_fruit_pos))

    def _set_direction(self, direction):
        if not Direction.is_opposite(direction, self._direction):
            self._direction = direction

    def play(self):

        while not self._game_over:
            self._clean_fruits()
            key = self._player.get_input()
            new_dir = Direction.from_key(key)
            if new_dir:
                self._set_direction(new_dir)

            self._snake.move(self._direction)
            snake_head = self._snake.head
            if self._check_collision(snake_head):
                self._game_over = True
            else:
                bonus = self._check_fruits(snake_head)
                self._snake.add_bonus(bonus)
                self._player.score += bonus

            self._board.set_snake_pos(self._snake.render())
            fruits_pos = list(map(lambda fruit: fruit.render(), self._fruits))
            self._board.set_fruits_pos(fruits_pos)
            self._board.set_score(self._player.score)

            self._board.render()
            time.sleep(0.125)

        return self._player
