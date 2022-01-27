from dd_gpio import DD_GPIO
from dd_gpio import GPIO_INPUT
from dd_gpio import GPIO_OUTPUT
import time

if __name__ == '__main__':

    gpio = DD_GPIO()
    
    while True:
        if(int(gpio.read(GPIO_INPUT.ADC7)) == 1):
            time.sleep(2) #green and orange
            gpio.write(GPIO_OUTPUT.ADC0, GPIO_OUTPUT.LOW)
            gpio.write(GPIO_OUTPUT.ADC1, GPIO_OUTPUT.HIGH)
            time.sleep(3) #red
            gpio.write(GPIO_OUTPUT.ADC0, GPIO_OUTPUT.HIGH)
            gpio.write(GPIO_OUTPUT.ADC1, GPIO_OUTPUT.LOW)
            time.sleep(3) #red and orange      
            gpio.write(GPIO_OUTPUT.ADC1, GPIO_OUTPUT.LOW)
            gpio.write(GPIO_OUTPUT.ADC0, GPIO_OUTPUT.LOW)
            time.sleep(3)
        else:
            gpio.write(GPIO_OUTPUT.ADC0, GPIO_OUTPUT.LOW)
            gpio.write(GPIO_OUTPUT.ADC1, GPIO_OUTPUT.HIGH)


