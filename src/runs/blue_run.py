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

    mv.straight(-10)
    mv.reset_gyro()

    mv.straight(460)
    mv.turn(-90, speed=200)
    mv.straight(150)
    mv.move_right_to(1000, 100)

    wait(200)

    mv.move_right_to(1000, 600)
#odjezd od štětce
#moving to map
    mv.straight(-100, cruise_speed=200)
    mv.turn(0, speed=180)
    mv.straight(160)
    mv.turn(-45, speed=100)
    #mv.move_left_to (200, 0)
    mv.move_right_to(700, 100)
    #mv.straight(100, cruise_speed=250)
    mv.move_left_to(600, 20)
    mv.straight(45, cruise_speed=200)
    mv.move_left_to(600, 25)
    mv.straight(45, cruise_speed=200 )
    #mv.straight(100, cruise_speed=250)
    mv.move_right_to(1000, 700)
    mv.move_left_to(600, 110)
#go home
    mv.straight(-100)
    mv.turn(180, speed=180)
    mv.robot.left_motor.run_angle(600, 120, wait=False)
    mv.straight(500, start_speed=600, cruise_speed=600, end_speed=600)

