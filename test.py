from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)

kit.continuous_servo[0].throttle = 1
time.sleep(5)
kit.continuous_servo[0].throttle = 0