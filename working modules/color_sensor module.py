import RPi.GPIO as GPIO
import time

# Define GPIO pins
S0 = 17
S1 = 27
S2 = 22
S3 = 5
OUT = 6

# Set GPIO mode and setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)
GPIO.setup(OUT, GPIO.IN)

# Set frequency scaling to 20%
GPIO.output(S0, GPIO.LOW)
GPIO.output(S1, GPIO.HIGH)

def read_color(channel):
    # Select the specified color channel
    if channel == 'red':
        GPIO.output(S2, GPIO.LOW)
        GPIO.output(S3, GPIO.LOW)
    elif channel == 'green':
        GPIO.output(S2, GPIO.HIGH)
        GPIO.output(S3, GPIO.HIGH)
    elif channel == 'blue':
        GPIO.output(S2, GPIO.LOW)
        GPIO.output(S3, GPIO.HIGH)
    else:
        raise ValueError("Invalid channel. Use 'red', 'green', or 'blue'.")

    # Wait for the sensor to settle
    time.sleep(0.1)

    # Measure the frequency
    frequency = 0
    for _ in range(10):
        frequency += GPIO.input(OUT)

    # Calculate the average frequency
    frequency /= 10

    # Convert frequency to RGB values
    if frequency > 0:
        value = 255 / frequency
    else:
        value = 0

    return value

try:
    while True:
        # Read and print the values for red, green, and blue channels
        red_value = read_color('red')
        green_value = read_color('green')
        blue_value = read_color('blue')

        print(f"Red Value: {red_value:.2f}, Green Value: {green_value:.2f}, Blue Value: {blue_value:.2f}")

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()