import time
# import RPi.GPIO as GPIO
import math


def convert_to_duty_cycle(value):
    """
    Condition – 1: If the engine calculated Energy Output Value &lt;/= 15,
        Then duty cycle = [{5 / (Energy Output Value + 15)} x 100]
    Condition – 2: If the engine calculated Energy Output Value &gt; 15,
        Then duty cycle = {(5 / Energy Output Value) x 100}
    :param value:
    :return:
    """
    if value <= 15:
        return (5 / (value + 15)) * 100
    else:
        return (5 / value) * 100


def apply_pwm(value, side):
    print(f"Received stimulation value of {value} to apply on side: {side}")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(32, GPIO.OUT)
    p1 = GPIO.PWM(32, 20)  # left

    GPIO.setup(12, GPIO.OUT)
    p2 = GPIO.PWM(12, 20)  # right

    GPIO.setup(33, GPIO.OUT)
    p3 = GPIO.PWM(33, 20)  # common

    GPIO.setup(35, GPIO.OUT)
    p4 = GPIO.PWM(35, 20)  # common

    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)

    duty_cycle_value = convert_to_duty_cycle(value)
    clean_value = math.floor(duty_cycle_value)
    print(f"Engine result value = {value} is converted to duty cycle value = {clean_value}")

    try:
        for dc in range(0, clean_value + 1, 5):
            print(f"Setting the GPIO brightness to {dc}")

            # Common GPIO for either side
            p3.ChangeDutyCycle(dc)
            p4.ChangeDutyCycle(dc)

            if side == 'right':
                p2.ChangeDutyCycle(dc)
            elif side == 'left':
                p1.ChangeDutyCycle(dc)
            elif side == 'both':
                p1.ChangeDutyCycle(dc)
                p2.ChangeDutyCycle(dc)
            else:
                print("Could not apply the stimulation.")
            time.sleep(2)
    except KeyboardInterrupt:
        pass

    print("Pausing for 60 seconds before stopping the PWM.")
    time.sleep(60)
    print("Stopping the PWM.")
    p1.stop()
    p2.stop()
    p3.stop()
    p4.stop()
    GPIO.cleanup()

