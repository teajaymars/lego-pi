This repository is attached to my Lego + Raspberry Pi + Xbox Controller project. 

 * Read the [full article](http://blog.zephod.com/post/37120089376/lego-xbox-raspberry-pi) on my blog.
 * Watch it [in action](http://www.youtube.com/watch?feature=player_embedded&v=X7YRqCCBDBU) on YouTube.

## Overview

#### `lego-controller.sh`

Main script to execute the RC car controller.

#### `control.py`

Reads `Event` objects from the Xbox controller, and updates the GPIO/I2C outputs on the Raspberry Pi as appropriate.

#### `lib/xbox_read.py`

Wrapper around `xboxdrv` driver. Reads from the controller and emits `Event` objects, which have a `key` (`A`, `X1`, or other controller button) and a `value` (`0` or `1` for buttons. `0` to `256` for triggers. `-32767` to `32768` for thumbsticks.



## Installation on a fresh Raspberry Pi

#### Get pip. Update Python. Get C headers. Install the interface library.
    sudo apt-get install python-pip
    sudo easy_install -U distribute
    sudo apt-get install python-dev
    sudo pip install RPi.GPIO

#### Install I2C communications libraries
    sudo apt-get install python-smbus
    sudo apt-get install i2c-tools
    sudo modprobe i2c-bcm2708
    sudo modprobe i2c-dev

#### Install the XBox controller driver
    sudo apt-get install xboxdrv

#### Prove that it works... (wiggle the controller sticks)
    sudo xboxdrv --wid 0 -l 2 --dpad-as-button --deadzone 12000

#### Execute the motor controller
    sudo ./lego-controller.sh
