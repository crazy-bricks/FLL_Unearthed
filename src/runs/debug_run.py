from helper import debug_log
from robot import Robot
from movement import Movement
from config import DEBUG

def debug_run(robot: Robot, mv: Movement):
    if not DEBUG:
        return
    debug_log("Starting Debug Run", name="debug_run")

    # mv.turn(90, wheel="right")
    mv.straight(5000)