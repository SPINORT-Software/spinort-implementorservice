import time
import RPi.GPIO as GPIO

def apply_pwm(value, side):
    print(f"Received stimulation value of {value} to apply on side: {side}")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(32, GPIO.OUT)
    p1 = GPIO.PWM(32, 1000) # left

    GPIO.setup(12, GPIO.OUT)
    p2 = GPIO.PWM(12, 1000) # right

    p1.start(0)
    p2.start(0)
    try:
        for dc in range(0, value + 1, 5):
            print(f"Setting the GPIO brightness to {dc}")
            if side == 'right':
                p2.ChangeDutyCycle(dc)
            elif side == 'left':
                p1.ChangeDutyCycle(dc)
            else:
                p1.ChangeDutyCycle(dc)
                p2.ChangeDutyCycle(dc)
            time.sleep(2)
    except KeyboardInterrupt:
        pass
    print(f"Stopping the PWM.")
    p1.stop()
    p2.stop()
    GPIO.cleanup()



