import sys
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pin = 3

for i in range(3):
    GPIO.output(pin, 1)
    sleep(.3)
    GPIO.output(pin, 0)
    sleep(.3)

GPIO.cleanup()
