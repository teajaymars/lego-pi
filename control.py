#!/usr/bin/python

import RPi.GPIO as GPIO
from lib.Adafruit_PWM_Servo_Driver import PWM
from lib import xbox_read
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)

# Initialise the GPIO output channels
GPIO.setmode(GPIO.BCM)
FORWARD = 21
BACKWARD = 17
GPIO.setup(FORWARD, GPIO.OUT)
GPIO.setup(BACKWARD, GPIO.OUT)
direction = None

# Setup direction of travel
def setDirection(new_direction):
    global direction # One global property, cut me some slack
    if direction:
        GPIO.output(direction,False)
    GPIO.output(new_direction,True)
    direction = new_direction

setDirection(FORWARD)

# Default calibration values 
servoMid = 425
servoWidth = 180

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

rt_intensity = 0
lt_intensity = 0
steer = servoMid

for event in xbox_read.event_stream(deadzone=12000):
    # Triggers control speed
    if event.key=='RT' or event.key=='LT':
        if event.key=='RT':
            rt_intensity = event.value
        else:
            lt_intensity = event.value
        # Change direction outputs when one trigger is pulled harder than the other
        new_direction = FORWARD if rt_intensity>=lt_intensity else BACKWARD
        if not direction==new_direction:
            print 'set direction: %s' % {FORWARD:'FORWARD',BACKWARD:'BACKWARD'}[new_direction]
            setDirection(new_direction)
        intensity = max(rt_intensity,lt_intensity) * 16
        pwm.setPWM(0, 0, intensity)
        print 'set speed: %d' % intensity
    # Left thumbstick controls the steering
    if event.key=='X1':
        steer = int( servoMid + (servoWidth*-event.value)/32768 )
        pwm.setPWM(1, 0, steer)
    if event.key=='Y' and event.is_press():
        servoMid = steer
        print 'Calibrate steering around %d' % steer
        
