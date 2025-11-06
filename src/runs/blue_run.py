from helper import debug_log
from robot import Robot
from movement import Movement

def blue_run(robot: Robot, mv: Movement):
    debug_log("Starting Blue Run")

    mv.straight(-20)
    mv.reset_gyro()
    robot.left_motor.reset_angle(0)
    robot.right_motor.reset_angle(0)

    