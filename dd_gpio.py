import time
import serial

class GPIO_INPUT:

    ADC5 = 5
    ADC6 = 6
    ADC7 = 7
    ADC8 = 8

class GPIO_OUTPUT:

    ADC0 = 0
    ADC1 = 1

    LOW = 0
    HIGH = 1

class DD_GPIO:
 
    def __init__(self):

        self.port = serial.Serial(
        port='/dev/serial0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=None)

    def read(self, pin):

        cmd = f"1{str(pin)}0\r\n"
        self.port.write(cmd.encode('utf-8'))

        rtn = self.port.readline()
        rtn = rtn.decode('utf-8')
        #print(rtn)

        time.sleep(0.1)

        rtn = int(rtn)
        return(rtn)

    def write(self, pin, state):

        cmd = f"2{str(pin)}{str(state)}\r\n"
        self.port.write(cmd.encode('utf-8'))

        rtn = self.port.readline()
        rtn = rtn.decode('utf-8')
        #print(rtn)

        time.sleep(0.1)

        return(rtn)
