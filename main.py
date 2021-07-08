#!/usr/bin/python3

from gpiozero import Button
from gpiozero import LineSensor
from gpiozero import OutputDevice
from gpiozero import LED

import time

#Pin Definitions
MOTORFWDPIN = 4     #Pin 7
MOTORBAKPIN = 17    #Pin 11
SUCCESSLEDPIN = 21  #Pin 13
CANDYBUTTONPIN = 22 #Pin 15
UPLINESENSPIN = 14  #Pin 8
DNLINESENSPIN = 15  #Pin 10

#Device Definitions
#candyRequester = Button(CANDYBUTTONPIN)
successLED = LED(SUCCESSLEDPIN)
motorfwd = OutputDevice(MOTORFWDPIN, active_high=False, initial_value=False)
motorbkwd = OutputDevice(MOTORBAKPIN, active_high=False, initial_value=False)
upSensor = LineSensor(UPLINESENSPIN)
candyRequester = LineSensor(DNLINESENSPIN)

def candydrop():
    motorfwd.on()
    print("motor spinning")
    #retval=upSensor.wait_for_no_line()#3) #Spin until line is broken or 3 seconds elapses
    #retval=upSensor.wait_for_line(3) #Spin until line is broken or 3 seconds elapses
    #if retval:
    #    print("Candy dropped")
    #else:
    #    print("No candy")
    time.sleep(1)
    motorfwd.off()
    print("motor stopped")

def main():
    counter = 0
    while True:
        print("BEGIN")
        #candyRequester.wait_for_no_line()
        candyRequester.wait_for_line()
        print("button pressed")
        candydrop()
        counter = counter + 1
        print(counter)
        #candyRequester.wait_for_line()
        candyRequester.wait_for_no_line()


if __name__ == "__main__":
  main()

