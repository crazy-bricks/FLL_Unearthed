import umath
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Direction

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
        self.robot.hub.imu.reset_heading(0)
        self.pose.reset_angle()
        wait(250)

    def straight(
            self,
            distance,
            start_speed=SPEED_SLOW,
            cruise_speed=SPEED,
            end_speed=SPEED_SLOW,
            accel_ratio=ACCEL_RATIO,
            decel_ratio=DECEL_RATIO,
            target_angle=None,
            timeout=None
    ):
        """
        Moves the robot straight for a certain distance while accelerating and decelerating using the trapezoidal motion profile.

        :param distance: Distance to move (in mm)
        :param start_speed: Starting speed (in mm/s)
        :param top_speed: Maximum speed (in mm/s)
        :param end_speed: Ending speed (in mm/s)
        :param target_angle: Target angle to maintain (in degrees)
        :param timeout: Timeout for the movement (in seconds)
        :return: None
        """
        self.robot.base.reset()

        if target_angle is None:
            target_angle = self.pose.angle
        else:
            self.pose.angle = target_angle

        direction = 1 if distance > 0 else -1

        accel_dist = abs(distance) * accel_ratio
        decel_dist = abs(distance) * decel_ratio
        cruise_dist = abs(distance) - accel_dist - decel_dist

        acceleration = (pow(cruise_speed, 2) - pow(start_speed, 2)) / (2 * accel_dist)
        deceleration = (pow(end_speed, 2) - pow(cruise_speed, 2)) / (2 * decel_dist)

        timer = StopWatch()

        controller = PID_Controller(PID_DRIVE, target_angle)

        while abs(distance) > abs(self.robot.base.distance()):
            # Get correction from PID
            correction = controller.update(self.robot.hub.imu.heading())

            debug_log("Target: {}, Yaw: {}".format(target_angle, self.robot.hub.imu.heading()), name="drive")

            if abs(self.robot.base.distance()) < accel_dist:
                # Accelerating
                speed = umath.sqrt(umath.pow(start_speed, 2) + (2 * acceleration * abs(self.robot.base.distance())))
            elif abs(self.robot.base.distance()) < (accel_dist + cruise_dist):
                # Cruising
                speed = cruise_speed
            elif abs(self.robot.base.distance()) < (accel_dist + cruise_dist + decel_dist):
                # Decelerating
                current_dist = abs(self.robot.base.distance()) - (accel_dist + cruise_dist)
                speed = umath.sqrt(umath.pow(cruise_speed, 2) + (2 * deceleration * current_dist))

            speed = clamp(speed, min(start_speed, end_speed), cruise_speed)

            self.robot.base.drive(direction * speed, correction)

            if timeout is not None and timer.time() > timeout:
                debug_log("Drive timeout reached", name="timeout")
                break
        self.robot.base.stop()
        self.robot.left_motor.hold()
        self.robot.right_motor.hold()
        if DEBUG:
            # Odometry
            X = self.robot.base.distance() * umath.cos(umath.radians(self.robot.hub.imu.heading()))
            Y = self.robot.base.distance() * umath.sin(umath.radians(self.robot.hub.imu.heading()))
            self.pose.set_coordinates(X, Y)
        wait(100)

    def steady(self, distance, speed=SPEED, target_angle=None, timeout=None):
        """
        Moves the robot straight for a certain distance at a steady speed.

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

            self.robot.base.drive(direction * speed, correction)

            if timeout is not None and timer.time() > timeout:
                debug_log("Drive timeout reached", name="timeout")
                break
        self.robot.base.stop()
        self.robot.left_motor.hold()
        self.robot.right_motor.hold()
        if DEBUG:
            # Odometry
            X = self.robot.base.distance() * umath.cos(umath.radians(self.robot.hub.imu.heading()))
            Y = self.robot.base.distance() * umath.sin(umath.radians(self.robot.hub.imu.heading()))
            self.pose.set_coordinates(X, Y)
        wait(100)

    def turn(
            self,
            angle,
            speed=SPEED_TURN,
            max_speed=SPEED,
            wheel="right",
            turn_tolerance=TURN_TOLERANCE,
            timeout=None
        ):
        """
        Turns the robot by a certain angle at a steady speed.
        
        :param angle: Angle to turn by (in degrees)
        :param speed: Speed to turn (in mm/s)
        :param max_speed: Maximum speed to turn (in mm/s)
        :param wheel: Wheel to use (left or right)
        :param timeout: Timeout for the movement (in seconds)
        :return: None
        """
        self.robot.base.reset()
        self.robot.left_drive.hold()
        self.robot.right_drive.hold()
        
        target_angle = self.pose.angle + angle
        output_limit = (-max_speed, max_speed)

        if wheel == "left":
            direction = 1
            motor = self.robot.left_drive
        elif wheel == "right":
            direction = -1
            motor = self.robot.right_drive
        else:
            raise ValueError("Invalid wheel: {}".format(wheel))

        timer = StopWatch()

        controller = PID_Controller(PID_TURN, target_angle, output_limit=output_limit)

        while abs(controller.get_error()) > turn_tolerance:
            output = controller.update(self.robot.hub.imu.heading())

            # debug_log("Target: {}, Yaw: {}, Error: {}, Output: {}, Direction: {}, Speed: {}".format(target_angle, self.robot.hub.imu.heading(), controller.get_error(), output, direction, output*direction), name="turn")
            print(controller.get_error(),)
            
            motor.run(output * direction)

            if timeout is not None and timer.time() > timeout:
                debug_log("Turn timeout reached", name="timeout")
                break
        motor.hold()
        self.pose.angle = target_angle
        wait(100)