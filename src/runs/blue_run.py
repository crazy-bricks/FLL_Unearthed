from helper import debug_log
from robot import Robot
from movement import Movement
from pybricks.tools import wait, StopWatch

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
    mv.straight(150, cruise_speed=300)
    mv.move_right_to(1000, 0)

    wait(1000)

    mv.move_right_to(1000, 600)
#odjezd
    mv.straight(-100)
    mv.turn(-24, speed=180)
    #mv.move_left_to (200, 0)

    mv.straight(200, cruise_speed=250)
    mv.move_left_to(600, -5)
    mv.move_right_to(1000, 120)
    mv.straight(90)
    mv.move_right_to(1000, 700)
    mv.move_left_to(600, 110)

    mv.straight(-230)
    mv.turn(-170, speed=180)
    mv.straight(500, start_speed=600, cruise_speed=600, end_speed=600)

