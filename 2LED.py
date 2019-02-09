import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

for x in range(0,5):
	print "Stop - RED"
	GPIO.output(14,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)
	GPIO.output(25,GPIO.LOW)
	GPIO.output(24,GPIO.HIGH)
	time.sleep(2)
	print "Move - GREEN"
	GPIO.output(24,GPIO.LOW)
	GPIO.output(25,GPIO.LOW)
	GPIO.output(14,GPIO.LOW)
	GPIO.output(18,GPIO.HIGH)
	time.sleep(2)
	print "Standby - YELLOW"
	GPIO.output(18,GPIO.LOW)
	GPIO.output(24,GPIO.LOW)
	GPIO.output(25,GPIO.LOW)
	GPIO.output(14,GPIO.HIGH)
	time.sleep(2)
	if x%2==0:
		print "Night - BLUE"
		GPIO.output(14,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
		GPIO.output(24,GPIO.LOW)
		GPIO.output(25,GPIO.HIGH)
		time.sleep(2)

GPIO.output(14,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.output(25,GPIO.LOW)
