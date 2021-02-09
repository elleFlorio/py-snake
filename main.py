import curses

from engine.game import Game
from engine.items.player import Player
from display.color import Color


def init_colors():
    curses.init_pair(Color.SNAKE.value, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(Color.WALL.value, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(Color.APPLE.value, curses.COLOR_RED, curses.COLOR_BLACK)


def init_player(screen):
    screen.nodelay(False)
    screen.clear()
    curses.echo()
    screen.addstr("Please enter your name\n")
    name = screen.getstr().decode(encoding="utf-8")
    curses.noecho()
    player = Player(name, "0", Color.SNAKE, screen)
    return player


def start_game(player, screen):
    screen.nodelay(True)
    screen.clear()
    game_instance = Game(player, screen)
    game_over = game_instance.play()
    return game_over


def display_score(game_over, screen):
    screen.nodelay(False)
    screen.clear()
    screen.addstr(
        "Congratulation {}, your score is {}!\n".format(game_over.name, game_over.score)
    )
    screen.addstr("Press ENTER to exit.\n")
    key = screen.getch()
    while key not in {curses.KEY_ENTER, 10, 13}:
        key = screen.getch()


def main(screen):
    init_colors()
    player = init_player(screen)
    game_over = start_game(player, screen)
    display_score(game_over, screen)


if __name__ == "__main__":
    curses.wrapper(main)
