from config import *
from robot import Robot
from pose import Pose
from movement import Movement

robot = Robot()
pose = Pose(0, 0, 0)
mv = Movement(robot, pose)

if __name__ == "__main__":
    raise SystemExit