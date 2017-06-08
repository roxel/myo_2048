import threading
import logging
from myo import init, Hub, DeviceListener
import myo as libmyo

from .frame import GameGrid
from .config import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP_ALT, KEY_DOWN_ALT, KEY_LEFT_ALT, \
    KEY_RIGHT_ALT
from .logic import move_up, move_down, move_left, move_right

logger = logging.getLogger("myo2048")


class Listener(DeviceListener):
    POSE_RIGHT = libmyo.Pose.wave_out
    POSE_LEFT = libmyo.Pose.wave_in
    POSE_UP = libmyo.Pose.fingers_spread
    POSE_DOWN = libmyo.Pose.fist

    def on_pair(self, myo, timestamp, firmware_version):
        print("myo paired")

    def on_unpair(self, myo, timestamp):
        print("myo unpaired")

    def _thread(self):
        t1 = threading.Thread(target=print, args=("thread",))
        t1.start()

    def on_pose(self, myo, timestamp, pose):
        if pose == Listener.POSE_RIGHT:
            print("pose right")
            self._thread()
            myo.vibrate('medium')
        elif pose == Listener.POSE_LEFT:
            print("pose left")
            self._thread()
            myo.vibrate('medium')
        elif pose == Listener.POSE_UP:
            print("pose up")
            self._thread()
            myo.vibrate('medium')
        elif pose == Listener.POSE_DOWN:
            print("pose down")
            self._thread()
            myo.vibrate('medium')


def grid_setup():
    logger.info("initializing game grid")
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
    return game_grid


def myo_setup():
    logger.info("initializing myo")
    init()
    return Hub(), Listener()


if __name__ == "__main__":
    logger.info("starting myo_2048")
    game_grid = grid_setup()
    hub, listener = myo_setup()
    try:
        hub.run(1000, listener)
        game_grid.mainloop()
    except:
        print()
    finally:
        hub.shutdown()

