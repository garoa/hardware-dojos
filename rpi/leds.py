from time import sleep
import atexit
import RPi.GPIO as GPIO

atexit.register(GPIO.cleanup)
GPIO.setmode(GPIO.BOARD)

LED_PINS = {'red': 3, 'yellow': 5, 'green': 7}


def activate(active_color):
    for color, pin in LED_PINS.items():
        GPIO.output(pin, color == active_color)


for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


if __name__=='__main__':

    for i in range(3):
        for color in LED_PINS:
            activate(color)
            sleep(.5)
