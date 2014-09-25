import RPi.GPIO as GPIO
import time
import random

#default GPIO pin numbering
GPIO.setmode(GPIO.BOARD)

led = 23
button = 3

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

GPIO.output(led, 0)

#pausing for a random time between 5 and 10 sec
time.sleep(random.uniform(5, 10))

GPIO.output(led, 1)

while GPIO.input(button):
	pass
if GPIO.input(button) == False:
	print "Button pressed"

time.sleep(2)

GPIO.output(led, 0)

GPIO.cleanup()