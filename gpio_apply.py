import RPi.GPIO as GPIO  # import the RPi.GPIO library

ledpin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setwarnings(False)


class GpioApply:
    def __init__(self):
        self._pwm = GPIO.PWM(ledpin, 1000)  # create the pwm instance with frequency 1000 Hz
        self._pwm.start(0)

    def apply_pwm(self, value):
        self._pwm.ChangeDutyCycle(value)


