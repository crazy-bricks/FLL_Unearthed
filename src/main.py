import builtins
print(dir(builtins))

from pybricks.parameters import Color, Button

from config import *
from robot import Robot
from pose import Pose
from movement import Movement
from helper import debug_log

from runs.yellow_run import yellow_run

robot = Robot()
pose = Pose(0, 0, 0)
mv = Movement(robot, pose)

def main():
    attachments = {
        Color.YELLOW: (yellow_run,)
    }

    stage = 0
    current_color = Color.NONE
    
    while True:
        top_color = robot.color_top.color()

        if current_color is not top_color:
            current_color = top_color
            robot.hub.light.on(top_color)
            stage = 0

        pressed = robot.hub.buttons.pressed()

        if Button.RIGHT in pressed:
            funcs = attachments.get(current_color)
            if funcs:
                funcs[stage](robot, mv)
            else:
                debug_log("No valid attachment detected, color {}".format(current_color), name="attachment")
        
        if Button.LEFT in pressed and current_color in attachments:
            stage = (stage + 1) % len(attachments[current_color])


if __name__ == "__main__":
    main()
    raise SystemExit