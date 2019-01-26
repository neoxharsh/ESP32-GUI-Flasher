# ESP32-Flasher-GUI
A GUI tool to flash firmware to ESP32

# What's News
esptool 2.6-beta
Python 3.7.
PyQt5.
Fix bugs.
Flash only bootloader/partiton/firmware or all.
Send text to serial port.
Shortcut Keys.

# New Update Check Below

This software are for those who are completly new, or maybe for those who are lazy enough to type the whole code.

The software is extremly to use.

First Select the Bootloader, Partition and Application file that you wish to flash, then select the appropriate "COM" port or for Linux "/dev/ttyUSB", after that select the baud rate if you wish to change it. Then finally write the Size of your flash memory in the format 
"4MB". Now you are ready to hit Erase and after that hit flash, after successfull completion the status will show the output, which can also be used to debug any error.

For Linux version, do make sure that you are running the program as sudo, to run it as sudo, navigate to the program directory and enter
```sudo ./ESPFlasherGUI```

You can use the precompiled executable in the release or use the ESPFlasherGUI.py to run the script directlym, provided you have the following dependency correctly installed.

1. PyQt5
2. PySerial

or maybe install esptool using the ```pip install pyserial``` and ```sudo apt install python-qt5``` command. 

The executable have been created using the pyinstaller.

# Material Design Update

The new update is based on material design and uses NodeJS as the backbone, and HTML and CSS as the front end, Electron is used to make it windows friendly. 

The whole app resides in the Material Design directory. You can grab the release if you are lazy, and if u are geeky and worry about spying stuff, go ahead use the source code. You just need to 
```npm install jquery serial-node ``` and install electron globaly ```npm install -g electron```. This will only work if you have set the path varibale to point to the npm bin directory. Thats it and then from the root of the directory run ```electron .```....

Enjoy the app...
 
