from os import popen
from sys import stdin
import re

s = re.compile('[ :]')

class Event:
    def __init__(self,key,value,old_value):
        self.key = key
        self.value = value
        self.old_value = old_value
    def is_press(self):
        return self.value==1 and self.old_value==0
    def __str__(self):
        return 'Event(%s,%d,%d)' % (self.key,self.value,self.old_value)

def apply_deadzone(x, deadzone, scale):
    if x < 0:
        return (scale * min(0,x+deadzone)) / (32768-deadzone)
    return (scale * max(0,x-deadzone)) / (32768-deadzone)

def event_stream(deadzone=0,scale=32768):
    _data = None
    subprocess = popen('nohup xboxdrv','r',65536)
    while (True):
        line = subprocess.readline()
        if 'Error' in line:
            raise ValueError(line)
        data = filter(bool,s.split(line[:-1]))
        if len(data)==42:
            # Break input string into a data dict
            data = { data[x]:int(data[x+1]) for x in range(0,len(data),2) }
            if not _data:
                _data = data
                continue
            for key in data:
                if key=='X1' or key=='X2' or key=='Y1' or key=='Y2':
                    data[key] = apply_deadzone(data[key],deadzone,scale)
                if data[key]==_data[key]: continue
                event = Event(key,data[key],_data[key])
                yield event
            _data = data

# Appendix: Keys
# --------------
# X1
# Y1
# X2
# Y2
# du
# dd
# dl
# dr
# back
# guide
# start
# TL
# TR
# A
# B
# X
# Y
# LB
# RB
# LT
# RT
