from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

try:
    while True:
        servo.angle = 0
        sleep(2)
        servo.angle = 40
        sleep(2)

except KeyboardInterrupt:
    # This block will be executed when a KeyboardInterrupt (Ctrl+C) is detected
    print("\nExiting the program.")
    servo.angle = None  # Stop the servo at its current position
    
     
# from gpiozero import Servo
# from time import sleep
# 
# servo = Servo(17)
# 
# while True:
#     servo.min()
#     sleep(1)
#     servo.mid()
#     sleep(1)
#     servo.max()
#     sleep(1)