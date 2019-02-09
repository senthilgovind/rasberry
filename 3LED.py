import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(3,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
        input_state = GPIO.input(3)
	if input_state == False:
		print("Button pressed")
		time.sleep(0.2)

		GPIO.output(18,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(18,GPIO.LOW)

		GPIO.output(14,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(14,GPIO.LOW)

		GPIO.output(24,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(24,GPIO.LOW)

