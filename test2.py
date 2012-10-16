#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GREEN = 18
RED = 23

GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

state = 0

while True:
    green = (state==1 or state==2)
    red = (state==2 or state==3)
    GPIO.output(GREEN, green)
    GPIO.output(RED, red)
    state = (state+1) % 4
    time.sleep(1)
