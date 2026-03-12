from machine import Pin, PWM, reset
from time import sleep

# SAFETY CHECK
is_goggled = "n"
while is_goggled is not "y":
    print("Please put on eye protections!\n")
    is_goggled = input("Are goggles on your face? (y/N)")
while is_free is not "n":
    print("Please have the stator of the motor clamped or fixed.")
    is_free = input("Is the stator of the motor freely moving? (Y/n)")
print("Hold tight! Unleash the beast!!!")
for i in reversed(range(3)):
    print(i+1)
    sleep(1)

# SETUP
throttle = PWM(Pin(16))
throttle.freq(50)
# TODO: config led for a naive HRI

# LOOP
print("\nramp up\n")
for dc in range(1_100_000, 1_900_000, 10_000): # forward up
    throttle.duty_ns(dc)
    print(dc)
    sleep(0.2)
print("\nramp down\n")
for dc in reversed(range(1_100_000, 1_900_000, 10_000)): # forward down
    throttle.duty_ns(dc)
    print(dc)
    sleep(0.2)
print("STOP")
sleep(1)
throttle.deinit()
reset()
