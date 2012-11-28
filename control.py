#!/usr/bin/python

from lib.Adafruit_PWM_Servo_Driver import PWM
import time
import re

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

diff = 1
intensity = 0

s = re.compile('[ :]')

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
servoMid = (servoMax + servoMin) / 2
servoW = (servoMax - servoMin) / 2
servoW *= .8

def deadzone(x, deadzone):
  if x>0:
    return max(0,x-deadzone)
  return min(0,x+deadzone)


pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
for event in xbox_read.event_stream():
while (True):
    line = stdin.readline()
    if not line:
        continue
    _data = filter(bool,s.split(line[:-1]))
    if len(_data)==42:
        data = { _data[x]:int(_data[x+1]) for x in range(0,len(_data),2) }
        intensity = data['RT'] * 16
        steer = deadzone( data['X1'], 8000)
     
        steer2 = int( servoMid + (servoW*steer)/24768 )
        print data['X1'], steer, steer2
        pwm.setPWM(0, 0, intensity)
        pwm.setPWM(15, 0, steer2)

