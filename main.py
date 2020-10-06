from gpiozero import Button
from gpiozero import LineSensor
from gpiozero import Motor
from gpiozero import LED

#Pin Definitions
MOTORFWDPIN = 7     #GPIO4
MOTORBAKPIN = 11    #GPIO17
SUCCESSLEDPIN = 13  #GPIO21
CANDYBUTTONPIN = 15 #GPIO22
UPLINESENSPIN = 8   #GPIO14
DNLINESENSPIN = 10  #GPIO15

#Device Definitions
candyRequester = Button(CANDYBUTTONPIN)
successLED = LED(SUCCESSLEDPIN)
motor = Motor(MOTORFWDPIN, MOTORBAKPIN)
upSensor = LineSensor(UPLINESENSPIN)
dnSensor = LineSensor(DNLINESENSPIN)

def candysuccess():

def candydrop():
	motor.forward()
	upSensor.wait_for_no_line(3) #Spin until line is broken or 3 seconds elapses
	motor.stop()
	
	
def main():
	

	
	while True:
		if candyRequester.is_pressed():
			candydrop()




if __name__ == "__main__":
	main()