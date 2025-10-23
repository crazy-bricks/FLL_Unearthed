from helper import debug_log
from robot import Robot
from movement import Movement

rightSpeed: int = 200
leftSpeed: int = 300

def orange_run(robot: Robot, mv: Movement):
    debug_log("Starting Orange Run")
    mv.reset_gyro()
    robot.left_motor.reset_angle(0)
    robot.right_motor.reset_angle(0)

    robot.right_motor.run_target(rightSpeed, 60)
    mv.straight(340)

    for x in range(3):
        robot.right_motor.run_target(10000, 0)
        robot.right_motor.run_target(10000, 60)
    robot.right_motor.run_target(10000, 0)
    robot.right_motor.run_target(10000, 38)

    mv.turn(-35)
    robot.left_motor.run_target(leftSpeed, -120)
    mv.straight(290)

    mv.turn(80)
    mv.straight(60)

    mv.turn(-20)
    mv.turn(20)
    robot.right_motor.run_target(rightSpeed, 60)
    robot.left_motor.run_target(leftSpeed, -60)

    mv.straight(100)
    
    