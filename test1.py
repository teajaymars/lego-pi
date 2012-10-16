#!/usr/bin/env python

from sys import stdin
import RPi.GPIO as GPIO
import time
import re
from pprint import pprint

GPIO.setmode(GPIO.BCM)

GREEN = 18
RED = 23

GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

s = re.compile('[ :]')

state = {GREEN:False,RED:False}
old_data = {}

while True:
    line = stdin.readline()
    if not line:
        continue
    _data = filter(bool,s.split(line[:-1]))
    if len(_data)==42:
	data = { _data[x]:_data[x+1] for x in range(0,len(_data),2) }
        if data['A']=='1' and old_data.get('A','0')=='0':
            state[GREEN] = not state[GREEN]
            print 'toggle green =',state[GREEN]
            GPIO.output(GREEN, state[GREEN])
        if data['B']=='1' and old_data.get('B','0')=='0':
            print 'toggle red =',state[RED]
            state[RED] = not state[RED]
            GPIO.output(RED, state[RED])
        old_data = data

