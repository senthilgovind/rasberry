import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(3,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
        input_state = GPIO.input(3)
	if input_state == False:
		print("Button pressed")
		time.sleep(2)
	else:
                print("Button UNpressed")
                time.sleep(2)



