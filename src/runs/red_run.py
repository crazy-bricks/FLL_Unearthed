from helper import debug_log
from robot import Robot
from movement import Movement
from pybricks.tools import wait, StopWatch
from pybricks.tools import Matrix
from pybricks.parameters import Color, Button

CHECK_MATRIX = Matrix([
    [0  , 0  , 0  , 0  , 0],
    [0  , 0  , 0  , 0  , 100],
    [0  , 0  , 0  , 100, 0],
    [100, 0  , 100, 0  , 0],
    [0  , 100, 0  , 0  , 0]
])

KROS_MATRIX = Matrix([
    [100, 0, 0, 0, 100],
    [0, 100, 0, 100, 0],
    [0, 0, 100, 0, 0],
    [0, 100, 0, 100, 0],
    [100, 0, 0, 0, 100]
])

def red_run(robot: Robot, mv: Movement):
    debug_log("Starting Red Run")

    chose = True
    run = 1

    while chose:
        #debug_log("chose loop")
        pressed = robot.hub.buttons.pressed()

        if run == 1:
            robot.hub.display.icon(CHECK_MATRIX)

        if run == 2:
            robot.hub.display.icon(KROS_MATRIX)

        if Button.RIGHT in pressed:
            run = 1
            robot.hub.display.icon(CHECK_MATRIX)
            break

        if Button.LEFT in pressed:
            run = 2
            robot.hub.display.icon(KROS_MATRIX)
            break

        #debug_log("RUN chosen")
        #debug_log(run)
        #debug_log(pressed)

    debug_log("Chosen run")
    debug_log(run)
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
    mv.straight(-20)
    mv.reset_gyro()
    mv.reset_left()
    mv.reset_right()
    #mv.move_right_to(600, 300)
    #mv.move_right_to(600, 0)

    """Flip small table"""
    mv.straight(26)
    mv.robot.right_motor.run_angle(400, -110, wait=False)
 
    mv.turn(-40)
    mv.straight(310)
 
    """flipuje"""
    mv.turn(-108)
 

    if run == 1:
        """Remove thing from the basket"""
        #ku
        mv.turn(-110) 
        mv.straight(250)
        mv.turn(-100, speed=600)
        mv.straight(250)
        #nabírání basket
        mv.turn(-145)
        mv.straight(-80)
        wait(500)
        #ku crane
        mv.straight(75)
        mv.turn(-160)
        mv.straight(80)
        mv.turn(-190)
        mv.straight(65)
        mv.turn(-194)
        #mv.turn_on_one(-10)
        #do mision
        mv.robot.left_motor.run(-800)
        #mv.robot.left_drive.run(-50)
        wait(2000)
        mv.robot.left_motor.stop()
        #back up
        mv.straight(-100)
        mv.turn(-56)
        #statue
        mv.move_right_to(600,15)
        mv.straight(240, cruise_speed=500)
        mv.turn(-35)
        wait(100)
        mv.move_right_to(600, -100)
        wait(100)

        mv.turn(-110)
        mv.straight(700, cruise_speed=1600, accel_ratio=2.0, target_angle=-120)


    else:
        """X mision"""
        #ku
        mv.turn(-110) 
        mv.straight(240)
        mv.turn(-100, speed=600)
        mv.straight(260, cruise_speed=1600)
        mv.turn(-150, speed= 300)

        mv.straight(90)
        mv.turn(-185)
        mv.straight(70)
        mv.turn(-205)
        wait(100)
        mv.straight(45)

        mv.robot.left_motor.run(-600)
        wait(500)
        mv.robot.left_motor.stop()

        #wait(100000)

        #do mision
        mv.robot.left_motor.run(-700)
        wait(900)
        mv.robot.left_motor.stop()
        #back up
        mv.straight(-90)
        mv.turn(-49)
        #statue
        mv.move_right_to(600, 12)
        mv.straight(200)
        mv.turn(-45, speed=500)#todle se menil zbyenk
        mv.move_right_to(600, -100)

        mv.turn(-110)
        mv.straight(800, cruise_speed=1600, accel_ratio=2.0)