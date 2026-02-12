from helper import debug_log
from robot import Robot
from movement import Movement

def green_run(robot: Robot, mv: Movement):
    debug_log("Starting Green Run")

    mv.reset_gyro()
    mv.straight(-30)

    mv.reset_gyro()
    mv.reset_left()
    mv.reset_right()

    mv.straight(600, cruise_speed=500)
    mv.turn(91)

    mv.straight(400, cruise_speed= 500)

    mv.turn(0)
    mv.straight(-30)
#ktomu
    mv.move_right_to(200, -210)
    mv.straight(100)
    mv.straight(-40)
    mv.straight(25)

    mv.move_right_to(200, -80)
    mv.straight(50)

    mv.turn(10)
    mv.straight(100)

    mv.turn(0, left_powerup=-300, right_powerup=300, speed=400)