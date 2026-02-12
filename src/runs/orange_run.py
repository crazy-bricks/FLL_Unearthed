from helper import debug_log
from robot import Robot
from movement import Movement
from pybricks.tools import wait, StopWatch

rightSpeed: int = 400
leftSpeed: int = 600

def orange_run(robot: Robot, mv: Movement):
    debug_log("Starting Orange Run")

    mv.straight(-20)
    mv.reset_gyro()
    mv.reset_left()
    mv.reset_right()

    mv.move_right_to(rightSpeed, 180)
    mv.straight(320)
    # mv.straight(1000)

    """Shoot stones from cliff"""
    for x in range(3):
        mv.move_right_to(10000, -20)
        wait(100)
        mv.move_right_to(10000, 190)
        wait(100)
    mv.move_right_to(10000, 0)
    wait(100)
    mv.move_right_to(10000, 58)

    """Dislodge rocks"""
    mv.turn(-35)
    mv.move_left_to(leftSpeed, -120)
    mv.straight(265)

    mv.turn(40, speed=200)
    mv.straight(50)

    mv.turn(10, speed= 400)
    mv.move_right_to(rightSpeed, 160)
    mv.turn(42, speed=160)
    mv.move_left_to(leftSpeed, -50)

    mv.straight(160, cruise_speed= 120, start_speed=60, end_speed=60)
    mv.move_left_to(leftSpeed, -70)

    """Put artefact behind rocks to the base area"""
    mv.turn(50)
    mv.turn(80, speed= 400)
    mv.move_left_to(leftSpeed, -200)
    mv.turn(50)
    mv.straight(-120)

    mv.turn(3, speed=180)
    mv.move_right_to(rightSpeed, 10)
    mv.straight(60)

    """flip rief"""
    mv.turn(-22, speed=400)
    mv.straight(-32)
    mv.turn(-70)
    mv.move_right_to(rightSpeed, 190)

    mv.straight(300)
    mv.turn(-157)
    mv.straight(12)

    """Put basket to the ground"""
    mv.move_right_to(rightSpeed, 10)
    mv.move_right_to(rightSpeed, 160)

    """Put up the table"""
    mv.turn(-260)
    mv.straight(-100)
    mv.turn(-220)
    mv.move_right_to(rightSpeed, 10)
    mv.straight(270)

    """Return to base"""
    mv.straight(-70)
    mv.move_right_to(rightSpeed, 160)
    mv.turn(-170)
    mv.move_right_to(rightSpeed, 10)
    mv.move_right_to(rightSpeed, 160)
    mv.turn(-270)
    mv.straight(220)
    mv.turn(-210)
    mv.straight(800, cruise_speed=500)

    # mv.turn(-45, speed=210)
    # mv.straight(100)
    # mv.straight(-300, cruise_speed=8000, start_speed=8000, end_speed=8000)

    # mv.turn(-90)
    # mv.straight(-150)
    # mv.turn(-10)
    # mv.straight(-900, cruise_speed=800, start_speed=500, end_speed=500)






    
    