import math

class AttitudeController:
    """
    Attitude controller that converts desired roll, pitch, yaw into
    desired body rates (p_ref, q_ref, r_ref) for the attitude rate controller.
    """
    def __init__(self, Kp_att_rp, Kp_yaw):
        """
        Args:
            Kp_att_rp: proportional gain for roll/pitch
            Kp_yaw: proportional gain for yaw
        """
        self.Kp_att_rp = Kp_att_rp
        self.Kp_yaw = Kp_yaw

    def compute_bodyrate_setpoints(self, desired_roll, desired_pitch, desired_yaw, roll, pitch, yaw):
        """
        Args:
            desired_roll, desired_pitch, desired_yaw: target angles (rad)
            roll, pitch, yaw: current angles (rad)

        Returns:
            p_ref, q_ref, r_ref: desired body rates (rad/s)
        """

        roll_error = desired_roll  - roll
        roll_error = (roll_error + math.pi) % (2 * math.pi) - math.pi

        pitch_error = desired_pitch - pitch
        pitch_error = (pitch_error + math.pi) % (2 * math.pi) - math.pi

        yaw_error = desired_yaw - yaw
        yaw_error = (yaw_error + math.pi) % (2 * math.pi) - math.pi

        # Convert to body rates
        p_ref = self.Kp_att_rp * roll_error
        q_ref = self.Kp_att_rp * pitch_error
        r_ref = self.Kp_yaw    * yaw_error

        return p_ref, q_ref, r_ref
