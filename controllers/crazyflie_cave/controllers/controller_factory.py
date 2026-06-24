# controller_factory.py
"""Factory for creating flight controllers."""

from enum import Enum
from controllers.flight_controller_interface import FlightController

from controllers.controller_config import (
    POSITION_GAINS,
    VELOCITY_GAINS,
    ATTITUDE_GAINS,
    RATE_GAINS,
    QUADCOPTER_PARAMS
)


class ControllerType(Enum):
    CASCADED = 1


def create_flight_controller(controller_type: ControllerType, dt: float) -> FlightController:
    """Create and return a flight controller based on the specified type.

    Args:
        controller_type: Which controller to instantiate.
        dt: Simulation timestep in seconds.

    Returns:
        A FlightController instance ready for use.
    """
    if controller_type == ControllerType.CASCADED:
        from controllers.position_controller import PositionController
        from controllers.velocity_controller import VelocityController
        from controllers.attitude_controller import AttitudeController
        from controllers.attitude_rate_controller import AttitudeRateController
        from controllers.motor_mixer import MotorMixer
        from controllers.cascaded_controller import CascadedController

        return CascadedController(
            dt,
            # 1- Position Controller
            PositionController(**POSITION_GAINS),
            # 2- Velocity Controller
            VelocityController(dt=dt, F_hover=QUADCOPTER_PARAMS["F_hover"], **VELOCITY_GAINS),
            # 3- Attitude Controller
            AttitudeController(**ATTITUDE_GAINS),
            # 4- Attitude Rate Controller
            AttitudeRateController(**RATE_GAINS),
            # 5- Motor mixer
            MotorMixer()
        )