#!/usr/bin/python

from lib.Adafruit_PWM_Servo_Driver import PWM
from lib import xbox_read
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)

# Initialise the GPIO output channels
GPIO.setmode(GPIO.BCM)
FOWARD = 17
BACKWARD = 21
GPIO.setup(FORWARD, GPIO.OUT)
GPIO.setup(BACKWARD, GPIO.OUT)
direction = None

# Setup direction of travel
def setDirection(new_direction):
    if direction:
        GPIO.output(direction,False)
    GPIO.output(new_direction,True)
    direction = new_dircetion

setDirection(FORWARD)


servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
servoMid = (servoMax + servoMin) / 2
servoW = (servoMax - servoMin) / 2
servoW *= .8

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

for event in xbox_read.event_stream(deadzone=12000):
    # Right trigger controls speed
    if event.key=='RT' or event.key=='LT':
        intensity = event.value * 16
        pwm.setPWM(0, 0, intensity)
    # Left trigger controls the steering
    if event.key=='X1':
        steer = int( servoMid + (servoW*event.value)/32768 )
        pwm.setPWM(15, 0, steer)
