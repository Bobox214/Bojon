import sys
import time

tasks = set(sys.argv[1:])

print("--- Initialization")
from jetbot import Robot
robot = Robot()
print("--- Initialization done")


if '1' in tasks:
    print('[Task 1] in 1s')
    time.sleep(1)
    robot.left(speed=0.3)
    time.sleep(1)
    robot.stop()
    time.sleep(1)
    robot.right(speed=0.3)
    time.sleep(1)
    robot.stop()
    time.sleep(1)
    robot.forward(speed=0.3)
    time.sleep(1)
    robot.stop()
    time.sleep(1)
    robot.backward(speed=0.3)
    time.sleep(1)
    robot.stop()
    print('[Task 1] done')

if '2' in tasks:
    print('[Task 2] in 1s')
    time.sleep(1)
    robot.left_motor.value = 0.5
    robot.right_motor.value = 0
    time.sleep(1)
    robot.stop()
    time.sleep(1)
    robot.left_motor.value = 0
    robot.right_motor.value = 0.5
    time.sleep(1)
    robot.stop()
    print('[Task 2] done')
