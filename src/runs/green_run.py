from helper import debug_log
from robot import Robot
from movement import Movement
from pybricks.tools import wait, StopWatch


def green_run(robot: Robot, mv: Movement):
    debug_log("Starting Green Run")

    #recalibrate
    mv.reset_gyro()
    mv.straight(-10)
    #redy motors
    mv.reset_gyro()
    mv.reset_left()
    mv.reset_right()
    #mv.driverigth(180, 255)

    #k díře
    mv.robot.left_motor.run_angle(300, -100, wait=False)
    mv.straight(815, decel_ratio=1.0)   
    mv.turn_on_one(86, wheel="left", max_speed=700)
    mv.robot.left_motor.run_angle(600,90, wait=False)
    mv.robot.right_motor.run_angle(200, -230)

    #mv.robot.right_drive.run_angle(300, -10)
    # mv.straight(5,  cruise_speed=80)
    mv.straight(210, cruise_speed=88, target_angle=70)#70
#delani mise
    mv.robot.left_motor.run_angle(100, -40, wait=False)#100,-51
    mv.robot.right_motor.run_angle(200, 145)
    wait(700)
#artefakt throwing
    mv.straight(-95, cruise_speed=90, target_angle=90)
    mv.robot.left_motor.run_angle(600, -135)
    mv.turn(145)
    mv.robot.left_motor.run_angle(900, 185, wait=False)
    mv.steady(-230, 800)
    mv.straight(-150, start_speed=600)
    mv.steady(-230, 800)
    mv.move_left_to(1000,90)
    mv.move_left_to(1000,0)
    mv.straight(-100, start_speed=600)
    mv.turn(100)
    mv.straight(-160)
    mv.turn(190)
    mv.straight(800)