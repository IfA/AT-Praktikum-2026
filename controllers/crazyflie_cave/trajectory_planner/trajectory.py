# trajectory.py
"""Trajectory definition for the Crazyflie controller."""

from trajectory_planner.setpoint import Setpoint


class Trajectory:
    """An ordered sequence of setpoints defining a trajectory."""

    def __init__(self, setpoints: list[Setpoint]):
        if not setpoints:
            raise ValueError("Trajectory must contain at least one setpoint.")
        self.setpoints = setpoints
        self.current_index = 0

    def current_setpoint(self) -> Setpoint:
        """Return the current active setpoint."""
        return self.setpoints[self.current_index]

    def advance(self) -> bool:
        """Move to the next setpoint. Returns True if advanced,
        False if already at the last setpoint."""
        if self.current_index < len(self.setpoints) - 1:
            self.current_index += 1
            return True
        return False

    def is_complete(self) -> bool:
        """Check if the trajectory has reached the final setpoint."""
        return self.current_index >= len(self.setpoints) - 1

    def reset(self):
        """Reset trajectory back to the first setpoint."""
        self.current_index = 0
