import time
import RPi.GPIO as GPIO

def apply_pwm(value):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(32, GPIO.OUT)
    p1 = GPIO.PWM(32, 1000)

    GPIO.setup(12, GPIO.OUT)
    p2 = GPIO.PWM(12, 1000)

    p1.start(0)
    p2.start(0)
    try:
        for dc in range(0, value + 1, 5):
            print(f"Setting the GPIO brightness to {dc}")
            p1.ChangeDutyCycle(dc)
            p2.ChangeDutyCycle(dc)
            time.sleep(2)
    except KeyboardInterrupt:
        pass
    print(f"Stopping the PWM.")
    p1.stop()
    p2.stop()
    GPIO.cleanup()



