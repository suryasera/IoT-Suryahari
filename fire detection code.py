#Import GPIO Library
import RPi.GPIO as GPIO
#Import time function Library
import time
#Configure GPIO in Raspberry Pi BCM Mode
GPIO.setmode(GPIO.BOARD) 
# Set the GPIO pins for the fire sensor, MQ2 gas sensor, and buzzer
fire_pin = 27
gas_pin = 22
buzzer_pin = 17
# Set up GPIO pins
GPIO.setup(fire_pin, GPIO.IN)
GPIO.setup(gas_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
#Loop
while True:
        flame_status = GPIO.input(fire_pin)
        gas_status = GPIO.input(gas_pin)
        print(flame_status)
        print(gas_status)

        if flame_status == GPIO.HIGH or gas_status == GPIO.HIGH:
            # Turn on the buzzer
            GPIO.output(buzzer_pin, GPIO.HIGH)
            print("Danger! Flame or gas detected!")
        else:
            # Turn off the buzzer
            GPIO.output(buzzer_pin, GPIO.LOW)
            print("Safe")

        # Delay for stability
        time.sleep(0.1)

# except KeyboardInterrupt:
#     # Clean up GPIO settings on keyboard interrupt
#     GPIO.cleanup()
