# setpoint.py
"""Class setpoint for the Crazyflie controller."""

# Reference Setpoint (single point) 
# [x_ref, y_ref, z_ref, yaw_ref]
# [m,     m,     m,     rad]

class Setpoint:
    """Represents a reference setpoint for the Crazyflie controller.
    """
    def __init__(self, x=0.2, y=-0.4, z=0.5, yaw=0.4):
        self.x = x         # Desired x position (meters)
        self.y = y         # Desired y position (meters)
        self.z = z         # Desired z position (meters)
        self.yaw = yaw     # Desired yaw angle (rad)

    def to_dict(self):
        """Convert to dictionary for use with flight controllers."""
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "yaw": self.yaw
        }