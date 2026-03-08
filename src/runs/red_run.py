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
    mv.straight(25)
 
    mv.turn(-40)
 
    mv.straight(310)
 
    """flipuje"""
    mv.turn(-108)
 

    if run == 1:
        """Remove thing from the basket"""
        #ku
        mv.straight(260)
        mv.turn(-100, speed=600)
        mv.straight(160)
        #nabírání basket
        mv.turn(-150)
        mv.straight(-75)
        wait(500)
        #ku crane
        mv.straight(130)
        mv.turn(-170)
        mv.straight(120)
        mv.turn(-190)
        mv.straight(55)
        #do mision
        mv.robot.left_motor.run(-600)
        wait(2000)
        mv.robot.left_motor.stop()
        #back up
        mv.straight(-100)
        mv.turn(-55)
        #statue
        mv.move_right_to(600, 200)
        mv.straight(100)
        mv.turn(-40)
        

        wait(100000)
       

    else:
        mv.turn(-90)
        mv.straight(20)
        mv.turn(-180)
        mv.straight(95)
        mv.turn(-190)
        """Do rope mission"""
        mv.move_left_to(10000, -1300)
        mv.straight(-90)
        """get redy for statue"""
        mv.turn(-55)
        mv.move_right_to(600, 200)
        mv.straight(20)
        #wait(10000)

    #wait(100000)

    """Return home"""
    

    wait(100)

    mv.straight(160, 100)
    mv.turn(-40)
    mv.move_right_to(600, 100)

    if run == 2:
        mv.move_right_to(600, 160)

    wait(100)

    mv.straight(-120)
    mv.turn(-75)
    mv.move_right_to(800, 0)

    mv.steady(-100, speed=1100)

    mv.turn(-104)
    mv.steady(-1200, speed=1100)