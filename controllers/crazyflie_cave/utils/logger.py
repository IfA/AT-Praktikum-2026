# logger.py
from utils.motor_setup import MOTOR_SIGNS

class Logger:
    def __init__(self, print_interval=0.1):
        """
        Initialize logger.

        Args:
            print_interval (float): Minimum time (seconds) between prints.
        """
        self.print_interval = print_interval
        self.time_since_last_print = 0.0
        self.motor_signs = MOTOR_SIGNS

    def log(self, state, z_ref, dt, sim_time):
        """
        Log the sensor state if the print interval has passed.

        Args:
            state (dict): Sensor state dictionary from CrazyflieSensors.read()
            dt (float): Time since last loop (seconds)
        """
        self.time_since_last_print += dt



        if self.time_since_last_print >= self.print_interval:
            pos_x, pos_y, pos_z = state["position"]
            vel_x, vel_y, vel_z = state["velocity"]
            roll, pitch, yaw = state["attitude"]
            roll_rate, pitch_rate, yaw_rate = state["attitude_rates"]

            # Altitude error (for feedback)
            error_z = z_ref - pos_z

            # Print sensor readings:
            print(f"Time: {sim_time:.2f} s --- Sensor Log ---")
            print(f"Current altitude: {pos_z:.3f} m, Vertical velocity: {vel_z:.3f} m/s, Altitude error: {error_z:.3f} m")
            print(f"Position X: {pos_x:.3f}, Position Y: {pos_y:.3f}, Position Z: {pos_z:.3f}")
            print(f"Velocity X: {vel_x:.3f}, Velocity Y: {vel_y:.3f}, Velocity Z: {vel_z:.3f}")
            print(f"Roll: {roll:.3f}, Pitch: {pitch:.3f}, Yaw: {yaw:.3f}")
            print(f"Roll rate: {roll_rate:.3f}, Pitch rate: {pitch_rate:.3f}, Yaw rate: {yaw_rate:.3f}")
            print("-----------------\n")

            self.time_since_last_print = 0.0

    def outputMotorVelocities(self, velocities):
            print(f"Motor velocities (with signs applied):")
            for i, (vel, sign) in enumerate(zip(velocities, self.motor_signs), start=1):
                print(f"m{i}: {sign*vel:.2f} rad/s")
