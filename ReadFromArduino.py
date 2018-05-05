import serial

def getArduinoValues():
    ser = serial.Serial('/dev/ttyUSB0',9600)
    while True:
        try:
            readstr = ser.readline();
            readstr = bytes.decode(readstr);
            print(readstr);
        
        except KeyboardInterrupt:
            print("You have exit the program")
            return


proceed=True;

while(proceed):    
    response = input("Do you want to fetch values");
    if(response == 'Y'):
        getArduinoValues();
    else:
        proceed=False;    


