#include<SoftwareSerial.h>

SoftwareSerial mySerial(0,1); //RX, TX


void setup() {
  
  mySerial.begin(9600);  
}

void loop() {
    
  mySerial.write("Hello there");
  
  mySerial.write('\n');
}
