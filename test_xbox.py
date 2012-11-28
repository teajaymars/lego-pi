#!/usr/bin/env python

print 'starting'
from lib import xbox_read

for event in xbox_read.event_stream(deadzone=10000):
    print event

print 'quitting'
