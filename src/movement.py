from pybricks.tools import wait, StopWatch
from config import *
from helper import clamp, debug_log
from pid import PID_Controller
from pose import Pose
from robot import Robot

class Movement:
    """A class for handling robot movement"""

    def __init__(self, robot: Robot, pose: Pose):
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

    def straight(self, distance, speed=SPEED, target_angle=None, timeout=None):
        """
        Moves the robot straight for a certain distance.

        :param distance: Distance to move (in mm)
        :param speed: Speed to move (in mm/s)
        :param target_angle: Target angle to maintain (in degrees)
        :param timeout: Timeout for the movement (in seconds)
        :return: None
        """
        self.robot.base.reset()

        if target_angle is None:
            target_angle = self.pose.angle
        else:
            self.pose.angle = target_angle

        direction = -1 if distance > 0 else 1

        timer = StopWatch()

        controller = PID_Controller(PID_DRIVE, target_angle)

        while abs(distance) > abs(self.robot.base.distance()):
            # Get correction from PID
            correction = controller.update(self.robot.hub.imu.heading())

            debug_log("Distance: {}, Error: {}, Correction: {}".format(self.robot.base.distance(), controller._last_error, correction), name="drive")

            self.robot.base.drive(direction * speed, correction)

            if timeout is not None and timer.time() > timeout:
                debug_log("Drive timeout reached", name="timeout")
                break
        self.robot.base.stop()
        self.robot.left_motor.hold()
        self.robot.right_motor.hold()
        wait(100)
