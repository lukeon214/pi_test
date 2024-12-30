from adafruit_servokit import ServoKit
import time
from sshkeyboard import listen_keyboard

kit = ServoKit(channels=16)

kit.servo[1].angle = 180
time.sleep(5)
kit.servo[1].angle = 0