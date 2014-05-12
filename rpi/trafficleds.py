from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

LED_PINS = {'red': 3, 'yellow': 5, 'green': 7}

for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


def activate(activate_color):
    for color, pin in LED_PINS.items():
        if color == activate_color:
            GPIO.output(pin, 1)
        else:
            GPIO.output(pin, 0)

def toggle(color):
    pin = LED_PINS[color]
    GPIO.output(pin, not GPIO.input(pin))


if __name__=='__main__':

    while True:
        for pin in [3, 5, 7]:
            GPIO.output(pin, 1)
            sleep(.5)
            GPIO.output(pin, 0)

    GPIO.cleanup()
