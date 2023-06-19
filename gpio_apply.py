import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 1000)


def apply_pwm(value):
    p.start(0)
    try:
        for dc in range(0, value + 1, 5):
            print(f"Setting the GPIO brightness to {dc}")
            p.ChangeDutyCycle(dc)
            time.sleep(2)
    except KeyboardInterrupt:
        pass


print(f"Stopping the PWM.")
p.stop()
GPIO.cleanup()
