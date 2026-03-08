from helper import debug_log
from robot import Robot
from movement import Movement
from pybricks.tools import wait, StopWatch

def white_run(robot: Robot, mv: Movement):
    debug_log("Starting White Run")

    mv.straight(100, cruise_speed=1400)
    mv.turn(90)