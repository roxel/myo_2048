Myo2048
=======

Myo version of 2048 game.

Library used for handling myo: <https://github.com/NiklasRosenstein/myo-python>

2048 game engine based on: <https://github.com/yangshun/2048-python>


## Installation

Clone the repository and run:

    git clone git@github.com:roxel/myo_2048.git
    cd myo_2048
    pip install -r requirements.txt
    
## Myo setup

Follow instructions found on: <http://myo-python.readthedocs.io/en/latest/index.html#installation>

## Playing

Connect Myo and start MyoConnect. Sync your Myo armband. Then run the game application:

    python -m myo_2048.game
    
Fingers spread / Arrow up / W – Move up
Wave out / Arrow right / D – Move right
Double tap / Arrow down / S – Move down
Wave in / Arrow left / D – Move left

Remember to calibrate Myo to properly detect arm poses.

## Game 

Game interface is based on Tkinter through Python standard library <https://docs.python.org/3.5/library/tkinter.html>
    
## Compatibility

Game was tested on MacOS Yosemite and included `requirements.txt` file contain `pyobjc` library needed to run start the game on Mac systems. 
On other platforms application should also was work under some minor adjustments but note that `myo-python` only works on devices with MyoSDK installed.

