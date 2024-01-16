import RPi.GPIO as GPIO
import time

# Encoder callback function
def encoder_callback(channel):
    global counter
    counter += 1 if GPIO.input(channel) == 1 else -1
    print(f"Encoder Count: {counter}")

# Set up GPIO
channel = 17  # Replace with your actual GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.add_event_detect(channel, GPIO.BOTH, callback=encoder_callback)

# Clean up GPIO
def cleanup_gpio():
    GPIO.remove_event_detect(channel)
    GPIO.cleanup()

# Main loop
counter = 0
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    cleanup_gpio()
    print("Exiting...")