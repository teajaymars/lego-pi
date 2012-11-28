from sys import stdin
import re

s = re.compile('[ :]')

def event_stream():
    _data = None
    while (True):
        line = stdin.readline()
        if not line:
            continue
        data = filter(bool,s.split(line[:-1]))
        if len(data)==42:
            # Break input string into a data dict
            data = { data[x]:int(data[x+1]) for x in range(0,len(data),2) }
            if not _data:
                _data = data
                continue
            for key in data:
                if data[key]==_data[key]: continue
                event = (key,data[key],_data[key])
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
