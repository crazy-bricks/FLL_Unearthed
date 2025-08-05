from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Direction

from config import *

class Robot:
    def __init__(self):
        """
        Initializes the Robot class
        """
        self.hub = PrimeHub(top_side=HUB_TOP, front_side=HUB_FRONT)
        self.right_drive = Motor(PORT_RIGHT_DRIVE, positive_direction=Direction.CLOCKWISE)
        self.left_drive = Motor(PORT_LEFT_DRIVE, positive_direction=Direction.COUNTERCLOCKWISE)
        self.base = DriveBase(self.left_drive, self.right_drive, WHEEL_DIAMETER, AXLE_TRACK)
        self.right_motor = Motor(PORT_RIGHT_MOTOR)
        self.left_motor = Motor(PORT_LEFT_MOTOR)
        self.color_sensor = ColorSensor(PORT_COLOR)