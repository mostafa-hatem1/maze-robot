import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
en = 12
in3 = 17
in4 = 27
en_b = 13
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.setup(en_b, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

right = GPIO.PWM(en, 1000)
left = GPIO.PWM(en_b, 1000)

right.start(25)
left.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

try:
    while True:
        x = input()
        
        x == 'r'
        print("run")
        def move_forward():
            if temp1 == 1:
                right.ChangeDutyCycle(50)
                left.ChangeDutyCycle(50)
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in3, GPIO.HIGH)
                GPIO.output(in4, GPIO.LOW)
                print("forward")
        def move_backward():
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            print("backward")

        def stop_moving():
            print("stop")
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.LOW)

        if x == 'f':
            print("forward")
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            temp1 = 1

        elif x == 'b':
            print("backward")
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            temp1 = 0

        elif x == 'l':
            print("low")
            right.ChangeDutyCycle(40)
            left.ChangeDutyCycle(40)

        elif x == 'm':
            print("medium")
            right.ChangeDutyCycle(65)
            left.ChangeDutyCycle(65)

        elif x == 'h':
            print("high")
            right.ChangeDutyCycle(85)
            left.ChangeDutyCycle(85)
        
        elif x == 'e':
            GPIO.cleanup()
            print("GPIO Clean up")
            break
        
        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")

except KeyboardInterrupt:
    print("\nExiting the program.")
    GPIO.cleanup()