from gpiozero import AngularServo, LED
import keyboard
from sshkeyboard import listen_keyboard

led = LED(21)
led.blink()

servo = AngularServo(19, min_angle=-90, max_angle=90)

def listen(key):
    if servo.angle <= 90:
        if key == "w":
            print("w")
            servo.angle += 5
    
    if servo.angle <= -90:
        if key=="s":
            print("s")
            servo.angle -= 5
            print(servo.angle)
    
listen_keyboard(listen)