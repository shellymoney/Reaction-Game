import RPi.GPIO as GPIO
import time
import random

#default GPIO pin numbering
GPIO.setmode(GPIO.BOARD)

led = 23

GPIO.setup(led, GPIO.OUT)

#pausing for a random time between 5 and 10 sec
time.sleep(random.uniform(5, 10))

GPIO.output(led, 1)

GPIO.cleanup()
#button = 