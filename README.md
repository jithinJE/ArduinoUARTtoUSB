# Arduino UART to USB

This for connecting a CP2102 UART to USB for Arduino, and read values using Serial communication

Below is a roughly drawn circuit for connecting the CP2102 to an Arduino.

Arduino Reset --> 0.1µF Capacitor --> DTR PIN<br>
Arduino TX (Pin 1) --> RXD<br>
Arduino RX (Pin 0) --> TXD<br>
Arduino 5V --> +5V<br>
Arduino GND --> GND<br>

 


![GitHub Logo](https://i.imgur.com/9ARoQhP.png)

## Upload sketch
Now, upload the sketch ArduinoUARTtoUSB.ino  to the Arduino to write a string message to the serial.

Now, this is a little tricky...While uploading, as soon as the IDE shows a "Compiling sketch..." message, press the Reset button on the Arduino. Hopefully you will get a "Done uploading." message.

## Read the message through serial

Execute the ReadFromArduino.py file to read the message from the Arduino.
