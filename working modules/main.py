# a* or dfs or any pathfinding algorithm
# instead of adding children using premade occupancy, move, then scan then add

# moving will have a function called moveTile based on normal motor movement
# turn right and turn left function using imu and motor functions, turn 90 degrees exactly
import gyroscope_module as gyro
import range_sensor as range
import motor_driver_module as motor
import time 

def move_tile():
  duration_seconds = 1.5
  # Record the start time
  start_time = time.time()
  # Perform the function repeatedly until the desired time has elapsed
  while time.time() - start_time < duration_seconds:
    motor.move_forward()
    
def rotate_180():
  value = gyro.gyro_angle_change
  motor.rotate()
  if gyro.gyro_angle_change == 180:
    motor.stop_moving()
    
def detect_right_wall():
  value = range.get_distance()
  if value >= 5:
    return True
  else:
    return False
def detect_left_wall():
  value = range.get_distance()
  if value >= 5:
    return True
  else:
    return False
def detect_front_wall():
  value = range.get_distance()
  if value >= 5:
    return True
  else:
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
    
    

#searching algorithm part 
while True:   
  move_tile()
  if detect_right_wall() == True and detect_left_wall() == True:
    move_tile()
  elif detect_right_wall() == True and detect_front_wall() == True:
    turn_left()
    move_tile()
  elif detect_left_wall() == True and detect_front_wall() == True:
    turn_right()
    move_tile()
  elif detect_left_wall() == True and detect_front_wall() == True and detect_right_wall() == True:
    rotate_180()
    move_tile()
      

    
    
  