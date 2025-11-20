import umath
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Direction

from config import *
from helper import clamp, debug_log
from pid import PID_Controller
from pose import Pose
from robot import Robot

def _clamp(x, lo, hi):
    return hi if x > hi else lo if x < lo else x


def _accel_factor(traveled_deg: float,
                  accel_angle: float,
                  start_accel_factor: float) -> float:
    if accel_angle <= 0:
        return 1.0
    t = _clamp(traveled_deg / float(accel_angle), 0.0, 1.0)
    return start_accel_factor + (1.0 - start_accel_factor) * t


def _is_stuck(stopwatch: StopWatch, lastCheckTime, lastError, error):
    currentTime = stopwatch.time()

    if currentTime - lastCheckTime < 1:
        return False, lastCheckTime, lastError
    
    if abs(error) >= 20:
        if lastError > 0 and lastError - error < 5:
            return True, currentTime, error
        elif lastError < 0 and lastError - error > -5:
            return True, currentTime, error
    return False, currentTime, error

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
        distance = abs(distance)

        timer = StopWatch()

        controller = PID_Controller(PID_DRIVE, target_angle)

        while distance > abs(self.robot.base.distance()):
            nowDist = abs(self.robot.base.distance())
            # Get correction from PID
            correction = controller.update(self.robot.hub.imu.heading())

            debug_log("Target: {}, Yaw: {}".format(target_angle, self.robot.hub.imu.heading()), name="drive")

            va = accel_ratio*nowDist + start_speed

            vd = -decel_ratio*(nowDist - distance) + end_speed

            speed = min(cruise_speed, va, vd)

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

    def turn_on_one(
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

    def turnTo(
        self,
        angle: int,
        tolerance: int = TURN_TOLERANCE,
        speed: int = SPEED_TURN,
        left_powerup: int = 0,
        right_powerup: int = 0,
        stop_at_end: bool = True,

        accel_angle: float = 10.0,
        start_accel_factor: float = 0.3,
    ):

        target_angle = self.pose.angle + angle
        now_dir: int = self.robot.hub.imu.heading()
        if 0 == target_angle:
            return

        rKp, rKi, rKd = PID_TURN

        start_angle = now_dir
        integral: float = 0.0
        last_error: float = 0.0

        stopwatch = StopWatch()
        last_check_ms = stopwatch.time()
        last_stuck_error = 0.0

        speed_limit: float = SPEED
        I_limit: float = 15.0

        wait(40)

        while True:
            now_dir = self.robot.hub.imu.heading()

            error: float = target_angle - now_dir

            if abs(error) <= tolerance:
                break

            derivative = error - last_error
            integral += error
            integral = _clamp(integral, -I_limit, I_limit)

            output: float = rKp * error + rKi * integral + rKd * derivative

            traveled = abs(now_dir - start_angle)
            a = _accel_factor(traveled, accel_angle, start_accel_factor)

            l_speed: float = -output * (speed + left_powerup) * a
            r_speed: float =  output * (speed + right_powerup) * a

            l_speed = _clamp(l_speed, -speed_limit, speed_limit)
            r_speed = _clamp(r_speed, -speed_limit, speed_limit)

            self.robot.left_drive.run(l_speed)
            self.robot.right_drive.run(r_speed)

            stuck, last_check_ms, last_stuck_error = _is_stuck(
                stopwatch,
                last_check_ms,
                last_stuck_error,
                error
            )

            if stuck:
                self.robot.left_drive.brake()
                self.robot.right_drive.brake()

                nudge = int(max(80, abs(speed) * a))
                self.robot.left_drive.run(-nudge)
                self.robot.right_drive.run(+nudge)
                wait(120)   # ~0.12 s

                start_angle = self.robot.hub.imu.heading()

            last_error = error

            wait(40)

        if stop_at_end:
            self.robot.left_drive.hold()
            self.robot.right_drive.hold()

