import RPi.GPIO as GPIO
import time
import random

#default GPIO pin numbering
GPIO.setmode(GPIO.BOARD)

led = 23

GPIO.setup(led, GPIO.OUT)

time.sleep(random.uniform(5, 10))

#button = 