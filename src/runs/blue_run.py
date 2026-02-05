from helper import debug_log
from robot import Robot
from movement import Movement

def blue_run(robot: Robot, mv: Movement):
    debug_log("Starting Blue Run")
    
    robot.left_motor.reset_angle(0)
    robot.right_motor.reset_angle(0)
    robot.right_motor.run_target(1000, 700)
    robot.left_motor.run_target(1000, 90)

    mv.straight(-20)
    mv.reset_gyro()

    mv.straight(460)
    mv.turn(-90, speed=200)
    mv.straight(150)
    robot.right_motor.run_target(1000, 0)

    