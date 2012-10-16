#!/bin/bash

modprobe i2c-dev
modprobe i2c-bcm2708

xboxdrv | python control.py
