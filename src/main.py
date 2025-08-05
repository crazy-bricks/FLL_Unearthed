from pybricks.parameters import Color, Button

from config import *
from robot import Robot
from pose import Pose
from movement import Movement
from helper import debug_log

from runs.debug_run import debug_run
from runs.yellow_run import yellow_run

robot = Robot()
pose = Pose(0, 0, 0)
mv = Movement(robot, pose)

def main():
    debug_log("Starting main loop", name="main")
    robot.hub.display.off()
    # robot.hub.light.on(Color.PINK)

    attachments = {
        Color.NONE: (debug_run,),
        Color.YELLOW: (yellow_run,)
    }


    stage = 0
    current_color = Color.NONE
    
    while True:
        top_color = robot.color_sensor.color()

        if current_color is not top_color:
            current_color = top_color
            robot.hub.light.on(top_color)
            stage = 0

        pressed = robot.hub.buttons.pressed()

        if Button.RIGHT in pressed:
            funcs = attachments.get(current_color)
            if funcs:
                debug_log("Running stage {} for color {}".format(stage, current_color), name="main")
                mv.reset()
                funcs[stage](robot, mv)
            else:
                debug_log("No valid attachment detected, color {}".format(current_color), name="main")
        
        if Button.LEFT in pressed and current_color in attachments:
            stage = (stage + 1) % len(attachments[current_color])


if __name__ == "__main__":
    main()
    raise SystemExit