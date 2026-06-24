import numpy as np

class VelocityController:
    """
    PID velocity controller for a quadcopter in Webots
    Outputs desired roll, pitch, and thrust commands
    """
    def __init__(self, Kp_xy, Kd_xy, Kp_z, Ki_z, Kd_z, dt, F_hover, tau_d):
        """
        Args:
            Kp_xy: proportional gain for lateral velocity (roll/pitch)
            Kd_xy: derivative gain for lateral velocity
            Kp_z: proportional gain for vertical velocity
            Ki_z: integral gain for vertical velocity
            Kd_z: derivative gain for vertical velocity
            dt: timestep in seconds
        """
        # Lateral
        self.Kp_xy = Kp_xy
        self.Kd_xy = Kd_xy
        self.prev_error_x = 0.0
        self.prev_error_y = 0.0

        # Vertical
        self.F_hover = F_hover
        self.Kp_z = Kp_z
        self.Ki_z = Ki_z
        self.Kd_z = Kd_z
        self.prev_error_z = 0.0
        self.integral_z = 0.0
        self.deriv_z = 0.0
        self.tau_d = tau_d   # derivative filter time constant

        self.dt = dt

    def compute_control_signals(self, vx_ref, vy_ref, vz_ref, vx, vy, vz):
        """
        Args:
            vx_ref, vy_ref, vz_ref: desired velocities (m/s)
            vx, vy, vz: current velocities (m/s)

        Returns:
            desired_roll
            desired_pitch
            thrust_command
        """

        # --- Lateral PID for desired roll/pitch ---
        error_x = vx_ref - vx
        error_y = vy_ref - vy

        # Deadband to prevent creeping drift
        if abs(error_x) < 0.01:
            error_x = 0.0
        if abs(error_y) < 0.01:
            error_y = 0.0

        deriv_x = (error_x - self.prev_error_x) / self.dt
        deriv_y = (error_y - self.prev_error_y) / self.dt

        # Clip lateral velocity errors to [-1, 1]
        error_x_clipped = np.clip(error_x, -1, 1)
        error_y_clipped = np.clip(error_y, -1, 1)

        desired_pitch = (self.Kp_xy * error_x_clipped + self.Kd_xy * deriv_x)
        desired_roll  = -(self.Kp_xy * error_y_clipped + self.Kd_xy * deriv_y)

        self.prev_error_x = error_x
        self.prev_error_y = error_y

        # --- Aufgabe 2a: Vertical velocity controller  ---
        # Implement a PID or PD controller that outputs thrust_command.        
        
        thrust_command = 0.001  # placeholder - replace with your controller output



        return desired_roll, desired_pitch, thrust_command
