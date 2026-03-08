from helper import debug_log
from robot import Robot
from movement import Movement

rightSpeed: int = 400
leftSpeed: int = 600

def yellow_run(robot: Robot, mv: Movement):
    debug_log("Starting Yellow Run")

    mv.reset_gyro()
    mv.reset_left()
    mv.reset_right()

    mv.tensionMotorRigth(-90, 50)
    #mv.move_left_to(180)
    mv.straight(550, 100)
    mv.turn(10, right_powerup=-200, left_powerup=200, speed=600)
    mv.straight(100, 1000)

    mv.turn(-3)
    mv.move_left_to(leftSpeed, 100)
    mv.straight(-50, 1000)
    mv.move_right_to(rightSpeed, 0)
    mv.straight(-500, 1000)