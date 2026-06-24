# sensors.py

class Sensors:
    def __init__(self, robot, timestep):
        """
        Initialize and enable all sensors.
        """
        self.timestep = timestep

        # Discover and print all available device names on the Crazyflie
        num_devices = robot.getNumberOfDevices()
        for i in range(num_devices):
            device = robot.getDeviceByIndex(i)
            print(f"Device {i}: '{device.getName()}'")

        # GPS
        self.gps = robot.getDevice("gps")
        self.gps.enable(timestep)

        # IMU
        self.imu = robot.getDevice("inertial_unit")
        self.imu.enable(timestep)

        # Gyro
        self.gyro = robot.getDevice("gyro")
        self.gyro.enable(timestep)

        # Camera
        self.camera = robot.getDevice("camera")
        self.camera.enable(timestep)

        # Range sensors
        self.range_right = robot.getDevice("range_right")
        self.range_right.enable(timestep)
        self.range_back = robot.getDevice("range_back")
        self.range_back.enable(timestep)
        self.range_left = robot.getDevice("range_left")
        self.range_left.enable(timestep)
        self.range_front = robot.getDevice("range_front")
        self.range_front.enable(timestep)

    def read(self):
        """
        Read all sensors and return a structured state dictionary.
        """

        # Position
        pos_x, pos_y, pos_z = self.gps.getValues()

        # Velocity
        vel_x, vel_y, vel_z = self.gps.getSpeedVector()

        # Attitude
        roll, pitch, yaw = self.imu.getRollPitchYaw()

        # Attitude rates
        roll_rate, pitch_rate, yaw_rate = self.gyro.getValues()

        # Range sensors
        range_data = {
            "front": self.range_front.getValue(),
            "back": self.range_back.getValue(),
            "left": self.range_left.getValue(),
            "right": self.range_right.getValue(),
        }

        return {
            "position": (pos_x, pos_y, pos_z),
            "velocity": (vel_x, vel_y, vel_z),
            "attitude": (roll, pitch, yaw),
            "attitude_rates": (roll_rate, pitch_rate, yaw_rate),
            "ranges": range_data,
        }
