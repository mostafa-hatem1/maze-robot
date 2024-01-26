import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins connected to the motor driver inputs
motor_in1 = 17
motor_in2 = 27
ena_pin = 12  # Use the ENA pin on your motor driver for PWM control

# Set up the GPIO pins as outputs
GPIO.setup(motor_in1, GPIO.OUT)
GPIO.setup(motor_in2, GPIO.OUT)
GPIO.setup(ena_pin, GPIO.OUT)

# Set up PWM for speed control
pwm_frequency = 1000  # You can adjust this frequency as needed
pwm_motor = GPIO.PWM(ena_pin, pwm_frequency)
pwm_motor.start(0)    # Start with 0% duty cycle (motor stopped)

try:
    # Run the motor in one direction at various speeds
    for duty_cycle in range(0, 101, 10):  # Vary duty cycle from 0% to 100%
        pwm_motor.ChangeDutyCycle(duty_cycle)
        GPIO.output(motor_in1, GPIO.HIGH)
        GPIO.output(motor_in2, GPIO.LOW)
        time.sleep(2)

    # Stop the motor for 2 seconds
    pwm_motor.ChangeDutyCycle(0)
    time.sleep(2)

    # Run the motor in the other direction at various speeds
    for duty_cycle in range(0, 101, 10):
        pwm_motor.ChangeDutyCycle(duty_cycle)
        GPIO.output(motor_in1, GPIO.LOW)
        GPIO.output(motor_in2, GPIO.HIGH)
        time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    # Clean up when the program is interrupted
    pwm_motor.stop()
    GPIO.cleanup()