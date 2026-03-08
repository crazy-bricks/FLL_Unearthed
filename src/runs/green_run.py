from helper import debug_log
from robot import Robot
from movement import Movement
from pybricks.tools import wait, StopWatch


def green_run(robot: Robot, mv: Movement):
    debug_log("Starting Green Run")

    #recalibrate
    mv.reset_gyro()
    mv.straight(-20)

    #mv.move_left_powerlift_to(600, -90, 100)

    mv.tensionMotorLeft(-300)
    debug_log("hi")
    #wait(1000)
    #redy motors
    mv.reset_gyro()
    mv.reset_left()
    mv.reset_right()

    #mv.driverigth(180, 255)

    #k díře
    mv.straight(600)
    mv.turn(90)
    #ku koleji
    mv.straight(360, cruise_speed= 600)
    #bourání sochy
    mv.turn(0)
    wait(200)
    mv.straight(-80, 100)
    #ktomu
    mv.move_right_to(200, -290)
    mv.straight(75, 100)
    
    mv.move_right_to(200, -120)
    wait(500)
    mv.straight(30)
    mv.move_right_to(70, -90)
    wait(500)
    mv.move_right_to(70, -120)
   
    mv.turn(20)
    mv.straight(50)
    mv.turn(5)

    mv.straight(90, 255)
    #pick up
    mv.move_left_to(100, 350)
    #mv.move_left_powerlift_to(600, -50, 100)

    wait(100)

    mv.move_left_powerlift_to(50, 200, 100)



    wait(100000)

    #mv.turn(15)
    #mv.straight(80)
    #mv.driverigth(270, 300)

    wait(100000)