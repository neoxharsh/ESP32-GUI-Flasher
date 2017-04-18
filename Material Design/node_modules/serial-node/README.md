![alt tag](https://camo.githubusercontent.com/56c24ffe3f0b7230fc8209bbffda43386b6fd13b/687474703a2f2f7333322e706f7374696d672e6f72672f337270776b706867352f53657269616c5f73696d626f6c2e706e67)
# Serial-node
Serial-node is a module for Node.js to control serial ports. (For now only for windows, soon to Linux and MacOS.)
### Installation
Via NPM:
```
npm install serial-node -g
```
### Functions
#### list()
This function list the available ports on your computer, returns an array of ports. 

Exemple:
```
var SerialPort= require('serial-node'), serial = new SerialPort();
serial.list();
for(i=0;i<list.length;i++) 
{
    console.log(match[i]); 
}
```
Note: if there is no available port, the returned array is equal 0.
#### use(port,values)
This function is to set up and use a port. 
The parameter 'port' is required and is the port name. 

Exemple:
```
var SerialPort= require('serial-node'), serial = new SerialPort();
serial.use('COM3');
'port' -> COM{N} (Windows).
```
###### values (optional)
The parameter 'values' is to set the parameters of a serial port.

 * baud, defaults to 9600. Must be a number you specify.
 * databits, defaults to 8. Must be one of: 8, 7, 6, or 5.
 * parity, defaults to none. Must be one of: none, even, mark, odd, or space.
 * stopbits, defaults to 1. Must be one of: 1,1.5, or 2.
 * timeout, defaults to off. Must be one of: on or off.
 * xon, defaults to off. Must be one of: on or off.
 * odsr, defaults to off. Must be one of: on or off.
 * octs, defaults to off. Must be one of: on or off.
 * dtr, defaults to off. Must be one of: on or off. 
 * rts, defaults to on. Must be one of: on or off.
 * idsr, defaults to off. Must be one of: on or off.
 
#### open()
This function is to open the serial port. 

Exemple: 
```
var SerialPort= require('serial-node'), serial = new SerialPort();
serial.use('COM3');
serial.open();
```
Note: This function must come after use().
#### write(value)
This function is to write the serial port. 

Exemple: 
```
var SerialPort= require('serial-node'), serial = new SerialPort();
serial.use('COM3');
serial.open();
serial.write('hi!');
```
Note: encoding is ASCII.
#### read()
This function is to read the serial port, returns the value(split by '\n' or '\0' of '\r'). 

Exemple: 
```
var SerialPort= require('serial-node'), serial = new SerialPort();
serial.use('COM3');
serial.open();
var read = serial.read();
console.log(read);
```
#### close()
This function is to close the serial port in use.

Exemple:
```
var serial = require('serial-node');
serial.use('COM3');
serial.open();
serial.write('hi!');
serial.close();
```
Note: This function must come after open() and use().
