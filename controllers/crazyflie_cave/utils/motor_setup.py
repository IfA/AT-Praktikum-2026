# motor_setup.py
"""Motor initialization and configuration for the Crazyflie in Webots."""

MOTOR_NAMES = ['m1_motor', 'm2_motor', 'm3_motor', 'm4_motor']
MOTOR_SIGNS = [-1, 1, -1, 1]  # CW / CCW directions


def initialize_motors(robot):
    """Initialize the four rotor motors in velocity control mode.

    Args:
        robot: The Webots Robot instance.

    Returns:
        List of motor devices ready for velocity commands.
    """
    # Access the four rotor motors by their device names
    motors = [robot.getDevice(name) for name in MOTOR_NAMES]

    # Set each motor to velocity control mode (infinite position)
    for motor in motors:
        motor.setPosition(float('inf'))     # Infinite position means velocity control
        motor.setVelocity(0.0)              # Initialize with zero velocity

    return motors


def set_motor_velocities(motors, velocities):
    """Apply velocity commands to motors with correct spin directions.

    Args:
        motors: List of motor devices.
        velocities: List of computed motor velocities.
    """
    for motor, velocity, sign in zip(motors, velocities, MOTOR_SIGNS):
        motor.setVelocity(sign * velocity)
