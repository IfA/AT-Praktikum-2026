class PositionController:
    """
    A position controller for a quadcopter
    """
    def __init__(self, Kp_x, Kp_y, Kp_z, Ki_x, Ki_y, deadband, vx_max, vy_max, vz_max, integral_limit):
        """
        Initialize the position controller with proportional and integral gains and safety parameters.

        Args:
            Kp_x (float): Proportional gain for x-axis.
            Kp_y (float): Proportional gain for y-axis.
            Kp_z (float): Proportional gain for z-axis.
            Ki_x (float): Integral gain for x-axis (small, optional).
            Ki_y (float): Integral gain for y-axis (small, optional).
            deadband (float): Minimum error threshold to ignore sensor noise (meters).
            vx_max, vy_max, vz_max (float): Maximum allowed velocity setpoints (m/s).
            integral_limit (float): Maximum magnitude of integral term to prevent wind-up.
        """
        self.Kp_x = Kp_x
        self.Kp_y = Kp_y
        self.Kp_z = Kp_z
        self.Ki_x = Ki_x
        self.Ki_y = Ki_y

        self.deadband = deadband
        self.vx_max = vx_max
        self.vy_max = vy_max
        self.vz_max = vz_max
        self.integral_limit = integral_limit

        # Initialize integrals
        self.integral_x = 0.0
        self.integral_y = 0.0

    def compute_velocity_setpoints(self, x_ref, y_ref, z_ref, pos_x, pos_y, pos_z, dt):
        """
        Compute velocity setpoints based on position error with deadband, integral, and clipping.

        Args:
            x_ref, y_ref, z_ref: desired positions (meters)
            pos_x, pos_y, pos_z: current positions (meters)
            dt: timestep in seconds (used for integral accumulation)

        Returns:
            tuple: Velocity setpoints (vx_ref, vy_ref, vz_ref)
        """
        # Compute position errors
        error_x = x_ref - pos_x
        error_y = y_ref - pos_y
        error_z = z_ref - pos_z

        # Apply deadband
        if abs(error_x) < self.deadband:
            error_x = 0.0
        if abs(error_y) < self.deadband:
            error_y = 0.0
        if abs(error_z) < self.deadband:
            error_z = 0.0

        # Update integrals with anti-windup
        self.integral_x += error_x * dt
        self.integral_x = max(-self.integral_limit, min(self.integral_limit, self.integral_x))

        self.integral_y += error_y * dt
        self.integral_y = max(-self.integral_limit, min(self.integral_limit, self.integral_y))

        # Compute velocity setpoints with proportional + integral
        vx_ref = self.Kp_x * error_x + self.Ki_x * self.integral_x
        vy_ref = self.Kp_y * error_y + self.Ki_y * self.integral_y
        vz_ref = self.Kp_z * error_z  # keep vertical proportional only; use altitude controller for integral

        # Clip velocity setpoints
        vx_ref = max(-self.vx_max, min(self.vx_max, vx_ref))
        vy_ref = max(-self.vy_max, min(self.vy_max, vy_ref))
        vz_ref = max(-self.vz_max, min(self.vz_max, vz_ref))

        return vx_ref, vy_ref, vz_ref
