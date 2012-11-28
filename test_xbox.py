#!/usr/bin/env python

print 'starting'
from lib import xbox_read

for event in xbox_read.event_stream():
    print event

print 'quitting'
