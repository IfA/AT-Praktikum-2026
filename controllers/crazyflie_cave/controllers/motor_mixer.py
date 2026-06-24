import math

class MotorMixer:
    """
    Motor mixer for Crazyflie in Webots.
    Inputs:
        total_thrust (N)
        tau_phi, tau_theta, tau_psi (N·m)
    Outputs:
        motor angular velocities (rad/s)
    """
    # Derived from y_i and x_i in the PROTO motor order (m1,m2,m3,m4)
    ROLL_SIGNS  = [-1, -1, +1, +1]   # +roll => left up, right down
    PITCH_SIGNS = [-1, +1, +1, -1]   # +pitch => rear up, front down

    def __init__(self, max_velocity=600.0):
        self.max_velocity = max_velocity

        # From proto file
        self.kT = 4e-05      # thrust constant - N / (rad/s)^2
        self.kQ = 2.4e-06    # drag constant - N*m / (rad/s)^2

        self.gamma = self.kQ / self.kT

        # From motor geometry (0.031, 0.031) X geometry not + geometry
        self.l = (0.031**2 + 0.031**2)**0.5

        # CW/CCW yaw signs (must match motor_setup.py)
        self.MOTOR_SIGNS = [-1, 1, -1, 1]

    def mix(self, total_thrust, tau_psi, tau_phi, tau_theta):

        # Motor Mixing Algorithm
        # MOTOR_SIGNS = [-1, 1, -1, 1]  # CW / CCW directions
        # +X (front), +Y (left)
        # M1 (X,Y) = (0.031, -0.031)    - Motor front right  # CW
        # M2 (X,Y) = (-0.031, -0.031)   - Motor back right   # CCW
        # M3 (X,Y) = (-0.031, 0.031)    - Motor back left    # CW
        # M4 (X,Y) = (0.031, 0.031)     - Motor front left   # CCW

        thrust_cmd = total_thrust/4
        roll_cmd = tau_phi/(4*self.l)
        pitch_cmd = tau_theta/(4*self.l)
        yaw_cmd = tau_psi/(4*self.gamma)


        F1 = (thrust_cmd
              + yaw_cmd
              - roll_cmd
              - pitch_cmd
              )
                

        F2 = (thrust_cmd
              - yaw_cmd
              - roll_cmd
              + pitch_cmd
              )
        
        F3 = (thrust_cmd
              + yaw_cmd
              + roll_cmd
              + pitch_cmd
              )
        
        F4 = (thrust_cmd
              - yaw_cmd
              + roll_cmd
              - pitch_cmd
              )
                
        thrusts = [F1, F2, F3, F4]

        velocities = []

        for F in thrusts:
            F = max(0.0, F)
            omega = math.sqrt(F / self.kT)
            omega = min(self.max_velocity, omega)
            velocities.append(omega)

        return velocities
