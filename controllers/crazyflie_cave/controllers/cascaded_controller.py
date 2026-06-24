import math
from controllers.flight_controller_interface import FlightController

class CascadedController(FlightController):
    def __init__(self,
                 dt,
                 position_controller,
                 velocity_controller,
                 attitude_controller,
                 attitude_rate_controller,
                 motor_mixer):
        self.dt = dt
        self.position_controller = position_controller
        self.velocity_controller = velocity_controller
        self.attitude_controller = attitude_controller
        self.attitude_rate_controller = attitude_rate_controller
        self.motor_mixer = motor_mixer
        self.time_since_last_print = 0.0
        self.print_interval = 0.02
        self.total_time = 0

    def compute_motor_commands(self, state, reference, debug=False):

        pos_x, pos_y, pos_z = state["position"]
        vel_x, vel_y, vel_z = state["velocity"]
        roll, pitch, yaw = state["attitude"]
        roll_rate, pitch_rate, yaw_rate = state["attitude_rates"]

        x_ref = reference["x"]
        y_ref = reference["y"]
        z_ref = reference["z"]
        yaw_ref = reference["yaw"]

        # --- Position Controller ---
        vx_ref, vy_ref, vz_ref = self.position_controller.compute_velocity_setpoints(
            x_ref, y_ref, z_ref, pos_x, pos_y, pos_z, self.dt
        )
       
        # Position loop operates in world frame.
        # Velocity loop operates in body frame.
        
        #  World to Body frame transformation
        cos_yaw = math.cos(yaw)
        sin_yaw = math.sin(yaw)

        # Rotate velocity reference into body frame
        vx_meas_body =  cos_yaw * vel_x + sin_yaw * vel_y
        vy_meas_body = -sin_yaw * vel_x + cos_yaw * vel_y

        vx_ref_body =  cos_yaw * vx_ref + sin_yaw * vy_ref
        vy_ref_body = -sin_yaw * vx_ref + cos_yaw * vy_ref


        self.total_time += self.dt
        self.time_since_last_print += self.dt
        if debug and self.time_since_last_print >= self.print_interval:

            # --- Debug prints: Position & velocity ---
            print(f"[Simulation time:] {self.total_time:.3f}")
            # print(f"[Position] pos=({pos_x:.6f}, {pos_y:.6f}, {pos_z:.6f}) ref=({x_ref:.6f}, {y_ref:.6f}, {z_ref:.6f})")
            print(f"[Angles] roll, pitch, yaw=({roll:.6f}, {pitch:.6f}, {yaw:.6f}) ref yaw=({yaw_ref:.6f})")
            print(f"[Velocity] measured_body=({vx_meas_body:.6f}, {vy_meas_body:.6f}, {vel_z:.6f}) ref_body=({vx_ref_body:.6f}, {vy_ref_body:.6f}, {vz_ref:.6f})")
            

        # --- Velocity Controller ---
        desired_roll, desired_pitch, thrust = self.velocity_controller.compute_control_signals(
            vx_ref_body, vy_ref_body, vz_ref,
            vx_meas_body, vy_meas_body, vel_z
        )

        max_angle = math.radians(10)

        desired_roll  = max(-max_angle, min(max_angle, desired_roll))
        desired_pitch = max(-max_angle, min(max_angle, desired_pitch))

        if debug and self.time_since_last_print >= self.print_interval:
            
            # --- Debug prints: Desired roll/pitch/thrust ---
            print(f"[Velocity Controller] desired_roll={math.degrees(desired_roll):.6f} deg, desired_pitch={math.degrees(desired_pitch):.6f} deg, thrust={thrust:.6f}")

        # --- Attitude Controller ---
        p_ref, q_ref, r_ref = self.attitude_controller.compute_bodyrate_setpoints(
            desired_roll, desired_pitch, yaw_ref,
            roll, pitch, yaw
        )

        if debug and self.time_since_last_print >= self.print_interval:
            # --- Debug prints: Body rate setpoints ---
            print(f"[Attitude Controller] p_ref={p_ref:.6f}, q_ref={q_ref:.6f}, r_ref={r_ref:.6f}, roll={roll:.6f}, pitch={pitch:.6f}, yaw={yaw:.6f}")

        # --- Rate Controller ---
        tau_phi, tau_theta, tau_psi = \
            self.attitude_rate_controller.compute_torques(
                p_ref, q_ref, r_ref,
                roll_rate, pitch_rate, yaw_rate, self.dt
            )
        
        if debug and self.time_since_last_print >= self.print_interval:
            # --- Debug prints: Torques ---
            print(f"[Rate Controller] tau_phi={tau_phi:.6f}, tau_theta={tau_theta:.6f}, tau_psi={tau_psi:.6f}, roll_rate={roll_rate:.6f}, pitch_rate={pitch_rate:.6f}, yaw_rate={yaw_rate:.6f}")
            print(f"[Lateral PID] error_x={vx_ref_body - vx_meas_body:.6f}, error_y={vy_ref_body - vy_meas_body:.6f}, desired_roll={math.degrees(desired_roll):.6f}, desired_pitch={math.degrees(desired_pitch):.6f}")


        if debug and self.time_since_last_print >= self.print_interval:
            print("Sending to mixer:",
                "T=",thrust,
                "tau_phi=", tau_phi,
                "tau_theta=", tau_theta,
                "tau_psi=", tau_psi
                )

        # --- Motor Mixer ---
        motor_velocities = self.motor_mixer.mix(
            thrust, tau_psi, tau_phi, tau_theta
        )

        if debug and self.time_since_last_print >= self.print_interval:
            # --- Debug prints: Motor outputs ---
            print(f"[Motor Mixer] m1={motor_velocities[0]:.3f}, m2={motor_velocities[1]:.3f}, m3={motor_velocities[2]:.3f}, m4={motor_velocities[3]:.3f}")
            self.time_since_last_print = 0.0

        return motor_velocities
