from helper import debug_log
from robot import Robot
from movement import Movement
from pybricks.tools import wait, StopWatch

rightSpeed: int = 400
leftSpeed: int = 600

def yellow_run(robot: Robot, mv: Movement):
    debug_log("Starting Yellow Run")

    mv.reset_gyro()
    mv.reset_left()
    mv.straight(-20, timeout=5)
    mv.tensionMotorRigth(-200, 25)
    mv.reset_right()
    #viíždí
    mv.straight(50)
    mv.turn(92)
    #Jede k tomu
    mv.straight(340, cruise_speed= 500, decel_ratio= 6.0)
    mv.turn(100)
    mv.straight(80)
    mv.turn(105)
    mv.move_left_to(1000, 80)
    mv.move_right_to(600, 180)
    mv.straight(-50, 200)
    mv.move_right_to(240, 200)
    mv.straight(-500, cruise_speed=1600)
