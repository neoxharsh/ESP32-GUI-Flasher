# ESP32-Flasher-GUI
A GUI tool to flash firmware to ESP32

This software are for those who are completly new, or maybe for those who are lazy enough to type the whole code.

The softawre is extremly to use.

First Select the Bootloader, Partition and Application file that you wish to flash, then select the appropriate COM port or for Linux "/dev/ttyUSB", after that select the baud rate if you wish to change it. Then finally write the Size of your flash memory in the format 
"4MB". Now you are ready to hit Erase and after that hit flash, after successfull completion the status will show the output, which can also be used to debug any error.

You can use the precompiled executable in the release or use the ESPFlasherGUI.py to run the script directlym, provided you have the following dependency correctly installed.

1. PyQt4
2. PySerial

or maybe install esptool using the ```pip install esptool``` command. 
