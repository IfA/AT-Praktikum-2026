class AttitudeRateController:
    """
    Attitude Rate Controller (PD/PID) for Crazyflie in Webots simulation units.
    Converts desired body rates into torque commands for motor mixing.
    """
    def __init__(self, Kp, Ki, Kd):
        """
        Args:
            Kp: proportional gain
            Ki: integral gain
            Kd: derivative gain
        """
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        # Integral terms
        self.integral_p = 0.0
        self.integral_q = 0.0

        # Previous errors for derivative
        self.prev_error_p = 0.0
        self.prev_error_q = 0.0
        self.prev_error_r = 0.0

    def compute_torques(self, p_ref, q_ref, r_ref, p, q, r, dt):
        """
        Args:
            p_ref, q_ref, r_ref: desired body rates (rad/s)
            p, q, r: current body rates (rad/s)
            dt: timestep (s)

        Returns:
            tau_phi, tau_theta, tau_psi: control signals
        """

        # --- Roll (p) ---
        error_p = p_ref - p
        self.integral_p += error_p * dt
        deriv_p = (error_p - self.prev_error_p) / dt
        tau_phi = self.Kp * error_p + self.Ki * self.integral_p + self.Kd * deriv_p
        self.prev_error_p = error_p

        # --- Pitch (q) ---
        error_q = q_ref - q
        self.integral_q += error_q * dt
        deriv_q = (error_q - self.prev_error_q) / dt
        tau_theta = self.Kp * error_q + self.Ki * self.integral_q + self.Kd * deriv_q
        self.prev_error_q = error_q

        # --- Yaw (r) ---
        error_r = r_ref - r
        tau_psi = self.Kp * error_r  # usually no integral for yaw
        self.prev_error_r = error_r

        return tau_phi, tau_theta, tau_psi
