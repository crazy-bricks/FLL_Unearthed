from helper import debug_log
from robot import Robot
from movement import Movement

def yellow_run(robot: Robot, mv: Movement):
    debug_log("Starting Yellow Run")

    mv.reset_gyro()
    robot.left_motor.reset_angle(0)
    robot.right_motor.reset_angle(0)

    mv.straight(320)
    mv.turn(30)
    mv.straight(200, target_angle=30)
    robot.right_motor.run_target(200)
    robot.left_motor.run_target(180)