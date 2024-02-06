import gyroscope_module as gyro
import range_sensor as range
import motor_driver_module as motor
import time

def move_tile():
    duration_seconds = 1.5
    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        motor.move_forward()

def rotate_180():
    value = gyro.gyro_angle_change
    motor.rotate()
    if gyro.gyro_angle_change == 180:
        motor.stop_moving()

def detect_right_wall():
    try:
        value = range.get_distance()
        if value >= 5:
            return True
        else:
            return False
    except Exception as e:
        print("Error in detecting right wall:", e)
        return False

def detect_left_wall():
    try:
        value = range.get_distance()
        if value >= 5:
            return True
        else:
            return False
    except Exception as e:
        print("Error in detecting left wall:", e)
        return False

def detect_front_wall():
    try:
        value = range.get_distance()
        if value >= 5:
            return True
        else:
            return False
    except Exception as e:
        print("Error in detecting front wall:", e)
        return False

def turn_right():
    value = gyro.gyro_angle_change
    motor.right.ChangeDutyCycle(20)
    motor.left.ChangeDutyCycle(80)
    if value == 90:
        motor.right.ChangeDutyCycle(50)
    motor.left.ChangeDutyCycle(50)

def turn_left():
    value = gyro.gyro_angle_change
    motor.right.ChangeDutyCycle(80)
    motor.left.ChangeDutyCycle(20)
    if value == 90:
        motor.right.ChangeDutyCycle(50)
    motor.left.ChangeDutyCycle(50)

def dfs():
    move_tile()
    visited = set()
    stack = []
    position = (0, 0)
    orientation = 0

    while True:
        visited.add(position)

        try:
            right_wall = detect_right_wall()
            left_wall = detect_left_wall()
            front_wall = detect_front_wall()
        except Exception as e:
            print("Error in sensor reading:", e)
            # Stop the motors and break out of the loop
            motor.stop_moving()
            break

        if not right_wall and (position[0] + 1, position[1]) not in visited:
            stack.append((position, orientation))
            position = (position[0] + 1, position[1])
            orientation = (orientation + 90) % 360
            turn_right()
            move_tile()
        elif not front_wall and (position[0], position[1] + 1) not in visited:
            stack.append((position, orientation))
            position = (position[0], position[1] + 1)
            move_tile()
        elif not left_wall and (position[0] - 1, position[1]) not in visited:
            stack.append((position, orientation))
            position = (position[0] - 1, position[1])
            orientation = (orientation - 90) % 360
            turn_left()
            move_tile()
        else:
            if not stack:
                break
            position, orientation = stack.pop()
            rotate_180()
            move_tile()

try:
    dfs()
except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    print("Execution interrupted by user.")
except Exception as e:
    # Handle other exceptions
    print("An error occurred during execution:", e)
finally:
    # Clean up resources, if necessary
    motor.cleanup()  # Perform cleanup of motor resources
