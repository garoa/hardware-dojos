from time import sleep
import atexit
import RPi.GPIO as GPIO

atexit.register(GPIO.cleanup)
GPIO.setmode(GPIO.BOARD)

LED_PINS = [('red', 3), ('yellow', 5), ('green', 7)]


def activate(active_color):
    for color, pin in LED_PINS:
        GPIO.output(pin, color == active_color)


for color, pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


if __name__=='__main__':

    for color, pin in LED_PINS * 3:
        print(color)
        activate(color)
        sleep(.5)
