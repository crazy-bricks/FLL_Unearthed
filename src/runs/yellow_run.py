from helper import debug_log
from robot import Robot
from movement import Movement

rightSpeed: int = 400
leftSpeed: int = 600

def yellow_run(robot: Robot, mv: Movement):
    debug_log("Starting Yellow Run")

    mv.reset_gyro()
    robot.left_motor.reset_angle(0)
    robot.right_motor.reset_angle(0)

    robot.right_motor.run_target(rightSpeed, -100)
    #robot.left_motor.run_target(180)
    mv.straight(550)
    mv.turn(10, right_powerup=-200, left_powerup=200, speed=400)
    mv.straight(100)

    mv.turn(0)
    robot.left_motor.run_target(leftSpeed, 100)
    mv.straight(-50)
    robot.right_motor.run_target(rightSpeed, 0)
    mv.straight(-500)