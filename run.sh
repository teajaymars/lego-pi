#!/bin/bash

modprobe i2c-dev
modprobe i2c-bcm2708

python control.py

