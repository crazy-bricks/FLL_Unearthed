from helper import debug_log
from robot import Robot
from movement import Movement
from pybricks.tools import wait, StopWatch

def white_run(robot: Robot, mv: Movement):
    debug_log("Starting White Run")

    mv.straight(50, cruise_speed=1400)
    
    mv.robot.left_motor.run(600)
    mv.robot.left_drive.run(1600)
    mv.robot.right_drive.run(600)

    wait(100000)

    mv.robot.left_drive.stop()
    mv.robot.right_drive.stop()