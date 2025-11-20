from helper import debug_log
from robot import Robot
from movement import Movement

rightSpeed: int = 200
leftSpeed: int = 600

def orange_run(robot: Robot, mv: Movement):
    debug_log("Starting Orange Run")

    mv.straight(-20)
    mv.reset_gyro()
    robot.left_motor.reset_angle(0)
    robot.right_motor.reset_angle(0)

    robot.right_motor.run_target(rightSpeed, 60)
    mv.straight(320)

    for x in range(3):
        robot.right_motor.run_target(10000, 0)
        robot.right_motor.run_target(10000, 60)
    robot.right_motor.run_target(10000, 0)
    robot.right_motor.run_target(10000, 50)

    mv.turn(-35)
    robot.left_motor.run_target(leftSpeed, -90)
    mv.straight(310)

    mv.turn(80)
    mv.straight(50)

    mv.turn(-25)
    mv.turn(25)
    robot.right_motor.run_target(rightSpeed, 60)
    robot.left_motor.run_target(leftSpeed, -60)

    mv.straight(150)
    mv.turn(10)
    robot.left_motor.run_target(leftSpeed, -200)
    mv.straight(-150)

    mv.turn(-mv.pose.angle)

    mv.straight(5)
    
    robot.right_motor.run_target(rightSpeed, -30)
    robot.right_drive.run_angle(1000, 200)

    mv.turn(-25)

    mv.straight(-100)

    mv.turn(-50)
    mv.straight(200)

    robot.left_motor.run_target(leftSpeed, -60)
    robot.left_motor.run_target(leftSpeed, -200)

    mv.turn(-60)
    mv.turn(60)
    mv.straight(-100)

    mv.turn(-90)
    mv.straight(200)






    
    