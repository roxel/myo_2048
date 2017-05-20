from .frame import GameGrid
from .config import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP_ALT, KEY_DOWN_ALT, KEY_LEFT_ALT, \
    KEY_RIGHT_ALT
from .logic import move_up, move_down, move_left, move_right

if __name__ == "__main__":
    commands = {
        KEY_UP: move_up,
        KEY_DOWN: move_down,
        KEY_LEFT: move_left,
        KEY_RIGHT: move_right,
        KEY_UP_ALT: move_up,
        KEY_DOWN_ALT: move_down,
        KEY_LEFT_ALT: move_left,
        KEY_RIGHT_ALT: move_right,
    }
    game_grid = GameGrid(commands)
