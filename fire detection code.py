#Import GPIO Library
import RPi.GPIO as GPIO
#Import time function Library
import time
#Configure GPIO in Raspberry Pi BCM Mode
GPIO.setmode(GPIO.BCM) 
# Set the GPIO pins for the fire sensor, MQ2 gas sensor, and buzzer
fire_pin = 27
gas_pin = 22
buzzer_pin = 17
#possible conditions
C1 = "fire detected"
C2 = "smoke detected"
C3 = "fire and smoke detected"
C4 = "no fire and no smoke detected"
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

        if flame_status == GPIO.LOW or gas_status == GPIO.LOW:
        GPIO.output(buzzer_pin, GPIO.HIGH)
                if flame_status == GPIO.LOW
                GPIO.output(buzzer_pin, GPIO.HIGH)
                print(C1)
                elif gas_status == GPIO.LOW
 	        GPIO.output(buzzer_pin, GPIO.HIGH)
                print(C2)
                elif flame_status == GPIO.LOW and gas_status == GPIO.LOW
 		GPIO.output(buzzer_pin, GPIO.HIGH)
                print(C3)                               
        else:
        GPIO.output(buzzer_pin, GPIO.LOW)
        print(C4)

# Delay for stability
time.sleep(0.1)

# except KeyboardInterrupt:
# Clean up GPIO settings on keyboard interrupt
# GPIO.cleanup()
