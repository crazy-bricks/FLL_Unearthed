from pybricks.parameters import Color, Button
from pybricks.tools import Matrix, wait

from config import *
from robot import Robot
from pose import Pose
from movement import Movement
from helper import debug_log

from runs.debug_run import debug_run
from runs.yellow_run import yellow_run
from runs.orange_run import orange_run
from runs.white_run import white_run
from runs.blue_run import blue_run
from runs.red_run import red_run
from runs.green_run import green_run

robot = Robot()
pose = Pose(0, 0, 0)
mv = Movement(robot, pose)

def main():
    debug_log("Starting main loop", name="main")
    robot.hub.display.off()
    # robot.hub.light.on(Color.PINK)

    attachments = {
        Color.NONE: (debug_run,),
        Color.YELLOW: (yellow_run,),
        Color.BLACK: (orange_run,),
        Color.WHITE: (white_run,),
        Color.BLUE: (blue_run,),
        Color.RED: (red_run,),
        Color.GREEN: (green_run,)
    }

    light_matrices = {
        Color.YELLOW: (YELLOW_MATRIX,),
        Color.BLACK: (ORANGE_MATRIX,),
        Color.WHITE: (WHITE_MATRIX,),
        Color.BLUE: (BLUE_MATRIX,),
        Color.RED: (RED_MATRIX,),
        Color.GREEN: (GREEN_MATRIX,),
        Color.NONE: (Matrix([[0] * 5] * 5),)
    }

    stage = 0
    current_color = Color.NONE
    
    while True:
        top_color = robot.color_sensor.color()
        robot.hub.light.on(top_color)
        if current_color == Color.NONE:
            robot.hub.light.on(Color.MAGENTA)

        if current_color is not top_color:
            current_color = top_color
            stage = 0
        
        if current_color in light_matrices:
                robot.hub.display.icon(light_matrices[current_color][stage])

        pressed = robot.hub.buttons.pressed()

        if Button.RIGHT in pressed:
            funcs = attachments.get(current_color)
            if funcs:
                debug_log("Running stage {} for color {}".format(stage, current_color), name="main")
                pose.reset()
                mv.reset_gyro()
                funcs[stage](robot, mv)
            else:
                debug_log("No valid attachment detected, color {}".format(current_color), name="main")
        
        if Button.LEFT in pressed and current_color in attachments:
            stage = (stage + 1) % len(attachments[current_color])
            wait(250)


if __name__ == "__main__":
    main()
    raise SystemExit