from pybricks.parameters import Port, Axis

########## ROBOT ##########

HUB_TOP = Axis.Z
HUB_FRONT = Axis.Y

PORT_LEFT_DRIVE = Port.A
PORT_RIGHT_DRIVE = Port.B
PORT_LEFT_MOTOR = Port.C
PORT_RIGHT_MOTOR = Port.D

PORT_COLOR = Port.F

WHEEL_DIAMETER = 52.75  # mm
AXLE_TRACK = 80  # mm

########## PID ##########

PID_DRIVE = {
    "kp": 4.5,
    "ki": 0.0005,
    "kd": 0.02,
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

SPEED = 500         # mm/s
SPEED_SLOW = 250    # mm/s

SPEED_TURN = 600    # deg/s

TURN_TOLERANCE = 2  # degrees

ACCEL_RATIO = 0.2
DECEL_RATIO = 0.4

##############  MISC  ##############

DEBUG = True