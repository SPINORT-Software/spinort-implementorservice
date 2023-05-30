# from gpio_apply import GpioApply
#
# gpio = GpioApply()
#
# gpio.apply_pwm(100)


import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 1000)  # channel=18 frequency=1000Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 90, 5):
            print(f"Setting the GPIO brightness to {dc}")
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()