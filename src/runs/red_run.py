from helper import debug_log
from robot import Robot
from movement import Movement
from pybricks.tools import wait, StopWatch

def red_run(robot: Robot, mv: Movement):
    debug_log("Starting Red Run")

    mv.straight(-20)
    mv.reset_gyro()
    robot.left_motor.reset_angle(0)
    robot.right_motor.reset_angle(0)

    mv.straight(25)
    mv.turn(-43)
    mv.straight(270)
    mv.turn(-113)
    mv.straight(390)
    mv.turn(-162)
    mv.straight(-60)
    mv.straight(160)
    # mv.straight(60)
    mv.turn(-180, speed=400)
    mv.straight(40)
    mv.turn(-192, speed=400)
    mv.straight(20)
    robot.left_motor.run_target(10000, -1000)