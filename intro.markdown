
# Get pip. Update Python. Get C headers. Install the interface library.
    sudo apt-get install python-pip
    sudo easy_install -U distribute
    sudo apt-get install python-dev
    sudo pip install RPi.GPIO

# Install the XBox controller driver
    sudo apt-get install xboxdrv

# Prove that it works...
    sudo xboxdrv --wid 0 -l 2 --dpad-as-button --deadzone 12000

# Execute
    sudo xboxdrv -l 2 | sudo ./test1.py 

# i2c
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
sudo modprobe i2c-bcm2708
sudo modprobe i2c-dev
