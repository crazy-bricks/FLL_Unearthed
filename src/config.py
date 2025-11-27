from pybricks.parameters import Port, Axis
from pybricks.tools import Matrix

########## ROBOT ##########

HUB_TOP = Axis.Z
HUB_FRONT = Axis.Y

PORT_LEFT_DRIVE = Port.A
PORT_RIGHT_DRIVE = Port.B
PORT_LEFT_MOTOR = Port.E
PORT_RIGHT_MOTOR = Port.D

PORT_COLOR = Port.F

WHEEL_DIAMETER = 49.5  # mm
AXLE_TRACK = 80  # mm

##############  MOVEMENT  ##############

SPEED = 600         # mm/s
SPEED_SLOW = 250    # mm/s

SPEED_TURN = 220    # mm/s

TURN_TOLERANCE = 3  # degrees

ACCEL_RATIO = 2.0
DECEL_RATIO = 2.0

########## PID ##########

PID_DRIVE = {
    "kp": 3.0,
    "ki": 0,
    "kd": 0,
    "i_limit": (-100, 100),
    "output_limit": None
}

PID_TURN = {
    "kp": 0.036, # 10
    "ki": 0.01,
    "kd": 0.02,
    "i_limit": (-100, 100),
    "output_limit": None
}

##############  MISC  ##############

DEBUG = True

YELLOW_MATRIX = Matrix([
    [0  , 100, 0  , 100, 0],
    [0  , 100, 0  , 100, 0],
    [0  , 0  , 100, 0  , 0],
    [0  , 0  , 100, 0  , 0],
    [0  , 0  , 0  , 0  , 0]
])

WHITE_MATRIX = Matrix([
    [100, 0  , 0  , 0  , 100],
    [100, 0  , 100, 0  , 100],
    [0  , 100, 0  , 100, 0],
    [0  , 100, 0  , 100, 0],
    [0  , 0  , 0  , 0  , 0]
])

ORANGE_MATRIX = Matrix([
    [0  , 100 , 100 ,0  , 0],
    [0  , 100, 0  , 100, 0],
    [0  , 100, 0  , 100, 0],
    [0  , 0  , 100, 100, 0],
    [0  , 0  , 0  , 0  , 0]
])

RED_MATRIX = Matrix([
    [100, 100, 0  , 0  , 0],
    [100, 0  , 100, 0  , 0],
    [100, 100, 0  , 0  , 0],
    [100, 0  , 100, 0  , 0],
    [100, 0  , 100, 0  , 0]
])

BLUE_MATRIX = Matrix([
    [100, 100, 0  , 0  , 0],
    [100, 0  , 100, 0  , 0],
    [100, 100, 0  , 0  , 0],
    [100, 0  , 100, 0  , 0],
    [100, 100, 0  , 0  , 0]
])

GREEN_MATRIX = Matrix([
    [100, 100, 100, 100, 0],
    [100, 0  , 0  , 0  , 0],
    [100, 0  , 100, 100, 0],
    [100, 0  , 0  , 100, 0],
    [100, 100, 100, 100, 0]
])
