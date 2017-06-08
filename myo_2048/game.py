import logging
from myo import init, Hub, DeviceListener
import myo as libmyo

from .frame import GameGrid
from .event_map import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP_ALT, KEY_DOWN_ALT, KEY_LEFT_ALT, \
    KEY_RIGHT_ALT
from .logic import move_up, move_down, move_left, move_right

logger = logging.getLogger("myo2048")
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


class Listener(DeviceListener):
    POSE_RIGHT = libmyo.Pose.wave_out
    POSE_LEFT = libmyo.Pose.wave_in
    POSE_UP = libmyo.Pose.fingers_spread
    POSE_DOWN = libmyo.Pose.double_tap

    def __init__(self, game_grid):
        super(Listener, self).__init__()
        self.game_grid = game_grid

    def on_pair(self, myo, timestamp, firmware_version):
        logger.info("myo paired")

    def on_unpair(self, myo, timestamp):
        logger.info("myo unpaired")

    def on_pose(self, myo, timestamp, pose):
        if pose == Listener.POSE_RIGHT:
            print("pose right")
            self.game_grid.event_generate("<KeyPress-Right>")
            myo.vibrate('short')
        elif pose == Listener.POSE_LEFT:
            print("pose left")
            self.game_grid.event_generate("<KeyPress-Left>")
            myo.vibrate('short')
        elif pose == Listener.POSE_UP:
            print("pose up")
            self.game_grid.event_generate("<KeyPress-Up>")
            myo.vibrate('short')
        elif pose == Listener.POSE_DOWN:
            print("pose down")
            self.game_grid.event_generate("<KeyPress-Down>")
            myo.vibrate('short')


def grid_setup():
    logger.info("initializing game grid")
    game_grid = GameGrid(commands)
    return game_grid


def myo_setup(game_grid):
    logger.info("initializing myo")
    init()
    return Hub(), Listener(game_grid)


if __name__ == "__main__":
    logger.info("starting myo_2048")
    game_grid = grid_setup()
    hub, listener = myo_setup(game_grid)
    try:
        hub.run(1000, listener)
        game_grid.mainloop()
    except Exception as e:
        logger.error("exiting: %s" % e)
    finally:
        hub.shutdown()

