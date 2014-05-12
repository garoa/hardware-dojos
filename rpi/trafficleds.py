from time import sleep

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

for pin in [3, 5, 7]:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

while True:
    for pin in [3, 5, 7]:
        GPIO.output(pin, 1)
        sleep(.5)
        GPIO.output(pin, 0)

GPIO.cleanup()
