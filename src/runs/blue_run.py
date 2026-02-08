from helper import debug_log
from robot import Robot
from movement import Movement

def blue_run(robot: Robot, mv: Movement):
    debug_log("Starting Blue Run")
    
    mv.reset_left()
    mv.reset_right()
    mv.move_right_to(1000, 700)
    mv.move_left_to(1000, 90)

    mv.straight(-20)
    mv.reset_gyro()

    mv.straight(460)
    mv.turn(-90, speed=200)
    mv.straight(150)
    mv.move_right_to(1000, 0)

    