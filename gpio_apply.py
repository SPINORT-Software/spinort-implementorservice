import RPi.GPIO as GPIO  # import the RPi.GPIO library

ledpin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setwarnings(False)

import time


class GpioApply:
    def __init__(self):
        self._pwm = GPIO.PWM(ledpin, 1000)  # create the pwm instance with frequency 1000 Hz
        self._pwm.start(0)

    def apply_pwm(self, value):
        for dc in range(0, value, 5):
            self._pwm.ChangeDutyCycle(dc)
            time.sleep(2)
