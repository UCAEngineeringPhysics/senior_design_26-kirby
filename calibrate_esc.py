from machine import Pin, PWM, reset
from utime import sleep, ticks_ms, ticks_diff

# SAFETY CHECK
is_free = "y"
while is_free is not "n":
    print("Please have the stator of the motor clamped or fixed.")
    is_free = input("Is the stator of the motor freely moving? (Y/n)")
print("Please calibrate ESC throttle follow the steps below:")
print("1. Turn off ESC.")
print("2. Unplug Pico.")
print("3. Plug Pico back in.")
print("4. Turn ESC back on.")
print("5. Run this MicroPython script.")

# SETUP

throttle = PWM(Pin(16))
throttle.freq(50)
# Range constants
DUTY_MAX = 1_940_000
DUTY_MIN = 1_100_000
throttle.duty_ns(DUTY_MAX)
is_esc_on = "n"
while is_esc_on is not "y":
    print("Please connect ESC.")
    is_esc_on = input("Is ESC connected? (Y/n)")
sleep(1)
throttle.duty_ns(DUTY_MIN)
sleep(2)

print("\n\u2713Throttle is calibrated\u2713\n")
print("Calibration succeeded, if you heard a long beep followed by 2 short beeps.")
print("If not, repeat and follow the instructions carefully.")
sleep(0.1)
reset()



