import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 1000)


def apply_pwm(value):
    p.start(0)
    try:
        for dc in range(0, value+1, 5):
            print(f"Setting the GPIO brightness to {dc}")
            p.ChangeDutyCycle(dc)
            time.sleep(2)
    except KeyboardInterrupt:
        pass


p.stop()
GPIO.cleanup()
