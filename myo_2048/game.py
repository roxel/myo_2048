import threading
from myo import init, Hub, DeviceListener
import myo as libmyo
from time import sleep

from .frame import GameGrid
from .config import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP_ALT, KEY_DOWN_ALT, KEY_LEFT_ALT, \
    KEY_RIGHT_ALT
from .logic import move_up, move_down, move_left, move_right


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


def myo_start():
    init()
    listener = Listener()
    hub = Hub()
    hub.run(1000, listener)

    try:
        while hub.running:
            sleep(0.5)
    except KeyboardInterrupt:
        print("Goodbye")
    finally:
        hub.shutdown()


if __name__ == "__main__":
    print("set grid")
    grid_setup()
    print("set myo")
    myo_start()









