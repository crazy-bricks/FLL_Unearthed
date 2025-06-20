from pybricks.parameters import Port, Color

########## ROBOT ##########

HUB_TOP = None
HUB_FRONT = None

PORT_DRIVE_LEFT = None
PORT_DRIVE_RIGHT = None
PORT_MOTOR_LEFT = None
PORT_MOTOR_RIGHT = None

PORT_COLOR_TOP = None

WHEEL_DIAMETER = 0
AXLE_TRACK = 0

########## PID ##########

PID_DRIVE = {
    "kp": 1,
    "ki": 0,
    "kd": 0,
    "i_max": 100,
    "output_max": None
}

PID_TURN = {
    "kp": 1,
    "ki": 0,
    "kd": 0,
    "i_max": 100,
    "output_max": 100
}

##############  MOVEMENT  ##############

SPEED = 300         # mm/s
SPEED_SLOW = 100    # mm/s

SPEED_TURN = 600    # deg/s

TURN_TOLERANCE = 2  # degrees

ACCEL_RATIO = 0.2
DECEL_RATIO = 0.2

##############  MISC  ##############

DEBUG = True