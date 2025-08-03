from pybricks.tools import wait, StopWatch
from config import *
from helper import clamp, debug_log
from pid import PID_Controller

class Movement:
    """A class for handling robot movement"""

    def __init__(self, robot, pose):
        """
        Initializes the Movement class

        :param robot: Robot object
        :param pose: Pose object
        """
        self.robot = robot
        self.pose = pose

    def reset_gyro(self):
        """
        Resets the gyro angle and the pose angle
        :return: None
        """
        wait(250)
        self.robot.gyro.reset_angle(0)
        self.pose.reset_angle()
        wait(250)