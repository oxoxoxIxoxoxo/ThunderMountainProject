from time import *
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
kit.continuous_servo[0].throttle = 0

while True:
    sleep(1)

    kit.continuous_servo[0].throttle = 1
    
    sleep(2)

    kit.continuous_servo[0].throttle = -0.5