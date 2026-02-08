from helper import debug_log
from robot import Robot
from movement import Movement
from pybricks.tools import wait, StopWatch

def red_run(robot: Robot, mv: Movement):
    debug_log("Starting Red Run")

    mv.straight(-20)
    mv.reset_gyro()
    mv.reset_left()
    mv.reset_right()

    """Flip smol table"""
    mv.straight(25)
    mv.turn(-43)
    mv.straight(310)
    mv.turn(-108)
    mv.straight(470)

    """Remove thing from the basket"""
    mv.turn(-158, right_powerup=80, left_powerup=-80, speed=400)
    mv.straight(-55)
    mv.straight(160)

    """Align for rope mission"""
    mv.turn(-181)
    mv.straight(60)
    # mv.straight(60)
    mv.turn(-195, speed=400, left_powerup= - 300, right_powerup= 300)
    mv.straight(70, target_angle=-200)
    # mv.turn(-192, speed=400)
    # mv.straight(20)
    """Do rope mission"""
    mv.move_left_to(10000, -1000)

    """Return home"""
    mv.straight(-140, target_angle=-180)
    mv.turn(-70)
    mv.steady(100, speed=800)

    mv.turn(-104)
    mv.steady(1200, speed=800)