import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(3,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.output(18,GPIO.HIGH) # GREEN ON
GPIO.output(24,GPIO.LOW) # RED OFF
GPIO.output(14,GPIO.LOW) # YELLOW OFF
GPIO.output(25,GPIO.LOW) # BLUE OFF

while True:
        input_state = GPIO.input(3)
	if input_state == False:
		print("Button pressed")
		time.sleep(0.2)

                GPIO.output(24,GPIO.LOW)

		GPIO.output(18,GPIO.LOW)
		GPIO.output(14,GPIO.HIGH) # YELLOW ON
		time.sleep(3) # WAIT FOR 3 seconds in YELLOW
                
                GPIO.output(14,GPIO.LOW) # YELLOW OFF
		GPIO.output(24,GPIO.HIGH) # RED ON
		
		for x in range(0,5):
                    GPIO.output(25,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(25,GPIO.LOW)
                    time.sleep(0.5)

                GPIO.output(24,GPIO.LOW)
        else:
                GPIO.output(18,GPIO.HIGH)
                GPIO.output(24,GPIO.LOW)
                GPIO.output(14,GPIO.LOW)