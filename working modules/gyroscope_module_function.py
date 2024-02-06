import smbus
import time
import math

# MPU-9250 register addresses
MPU9250_ADDRESS = 0x68  # Address when AD0 pin is connected to GND
MPU9250_WHO_AM_I = 0x75  # Should return 0x71

# MPU-9250 configuration registers
MPU9250_PWR_MGMT_1 = 0x6B
MPU9250_GYRO_CONFIG = 0x1B
MPU9250_ACCEL_CONFIG = 0x1C

# MPU-9250 data registers
MPU9250_ACCEL_XOUT_H = 0x3B
MPU9250_GYRO_XOUT_H = 0x43

# Create an instance of the SMBus
bus = smbus.SMBus(1)  # Change the number (1 or 0) based on your Raspberry Pi model

def read_byte(reg):
    return bus.read_byte_data(MPU9250_ADDRESS, reg)

def read_word(reg):
    high_byte = bus.read_byte_data(MPU9250_ADDRESS, reg)
    low_byte = bus.read_byte_data(MPU9250_ADDRESS, reg + 1)
    return (high_byte << 8) + low_byte

def initialize_mpu9250():
    # Power management setup
    bus.write_byte_data(MPU9250_ADDRESS, MPU9250_PWR_MGMT_1, 0x00)

    # Gyroscope configuration
    bus.write_byte_data(MPU9250_ADDRESS, MPU9250_GYRO_CONFIG, 0x08)  # Set full-scale range to ±500 degrees/s

    # Accelerometer configuration
    bus.write_byte_data(MPU9250_ADDRESS, MPU9250_ACCEL_CONFIG, 0x08)  # Set full-scale range to ±4g

def read_sensor_data():
    # Read accelerometer data
    accel_x = read_word(MPU9250_ACCEL_XOUT_H)
    accel_y = read_word(MPU9250_ACCEL_XOUT_H + 2)
    accel_z = read_word(MPU9250_ACCEL_XOUT_H + 4)

    # Read gyroscope data
    gyro_x = read_word(MPU9250_GYRO_XOUT_H)
    gyro_y = read_word(MPU9250_GYRO_XOUT_H + 2)
    gyro_z = read_word(MPU9250_GYRO_XOUT_H + 4)

    return gyro_x,
      


def calculate_gyro_angle(gyro_data, time_interval):
    gyro_x_rad_per_sec = gyro_data["gyro_x"] / 131.0 * (math.pi / 180.0)  # Convert raw reading to rad/s
    gyro_angle_change = gyro_x_rad_per_sec * time_interval  # Angular displacement = angular velocity * time

    return gyro_angle_change

def read_gyro_angle():
    total_angle = 0.0
    try:
        while True:
            start_time = time.time()
            
            sensor_data = read_sensor_data()
            
            gyro_angle_change = calculate_gyro_angle(sensor_data, time_interval=1)  # Assuming 1 second time interval
            total_angle += gyro_angle_change

            print("Accelerometer (g): X={}, Y={}, Z={}".format(sensor_data["accel_x"], sensor_data["accel_y"], sensor_data["accel_z"]))
            print("Gyroscope (deg/s): X={}, Y={}, Z={}".format(sensor_data["gyro_x"], sensor_data["gyro_y"], sensor_data["gyro_z"]))
            print("Gyroscope Angle (degrees): {:.2f}".format(math.degrees(total_angle)))
            print("")

            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("Exiting...")
    return gyro_angle_change

if __name__ == "__main__":
    who_am_i = read_byte(MPU9250_WHO_AM_I)
    if who_am_i != 0x71:
        print(f"MPU-9250 not detected. Expected 0x71, got 0x{who_am_i:02X}")
    else:
        print("MPU-9250 detected!")

        # Initialize the sensor
        initialize_mpu9250()

        # Read gyroscope angle
        read_gyro_angle()
