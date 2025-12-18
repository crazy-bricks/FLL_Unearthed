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
    mv.straight(300)
    mv.turn(-109)
    mv.straight(380)
    mv.turn(-160)
    mv.straight(-50)
    mv.straight(160)
    # mv.straight(60)
    # mv.turn(-195, speed=400, left_powerup= - 300, right_powerup= 300)
    mv.straight(70, target_angle=-190)
    # mv.turn(-192, speed=400)
    # mv.straight(20)
    robot.left_motor.run_target(10000, -1000)

    mv.straight(-90, target_angle=-180)
    mv.turn(-70)
    mv.straight(80, end_speed=800, start_speed=800, cruise_speed=800)
    mv.straight(1200, end_speed=800, start_speed=800, cruise_speed=800, target_angle=-104)