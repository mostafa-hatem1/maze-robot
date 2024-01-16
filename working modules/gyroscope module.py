import smbus
import time

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

def read_sensor_data():
    # Read accelerometer data
    accel_x = read_word(MPU9250_ACCEL_XOUT_H)
    accel_y = read_word(MPU9250_ACCEL_XOUT_H + 2)
    accel_z = read_word(MPU9250_ACCEL_XOUT_H + 4)

    # Read gyroscope data
    gyro_x = read_word(MPU9250_GYRO_XOUT_H)
    gyro_y = read_word(MPU9250_GYRO_XOUT_H + 2)
    gyro_z = read_word(MPU9250_GYRO_XOUT_H + 4)

    return {
        "accel_x": accel_x,
        "accel_y": accel_y,
        "accel_z": accel_z,
        "gyro_x": gyro_x,
        "gyro_y": gyro_y,
        "gyro_z": gyro_z,
    }

def initialize_mpu9250():
    # Power management setup
    bus.write_byte_data(MPU9250_ADDRESS, MPU9250_PWR_MGMT_1, 0x00)

    # Gyroscope configuration
    bus.write_byte_data(MPU9250_ADDRESS, MPU9250_GYRO_CONFIG, 0x08)  # Set full-scale range to ±500 degrees/s

    # Accelerometer configuration
    bus.write_byte_data(MPU9250_ADDRESS, MPU9250_ACCEL_CONFIG, 0x08)  # Set full-scale range to ±4g

# Check if the sensor is connected and responding
who_am_i = read_byte(MPU9250_WHO_AM_I)
if who_am_i != 0x71:
    print(f"MPU-9250 not detected. Expected 0x71, got 0x{who_am_i:02X}")
else:
    print("MPU-9250 detected!")

    # Initialize the sensor
    initialize_mpu9250()

    try:
        while True:
            sensor_data = read_sensor_data()
            print("Accelerometer (g): X={}, Y={}, Z={}".format(sensor_data["accel_x"], sensor_data["accel_y"], sensor_data["accel_z"]))
            print("Gyroscope (deg/s): X={}, Y={}, Z={}".format(sensor_data["gyro_x"], sensor_data["gyro_y"], sensor_data["gyro_z"]))
            print("")

            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")