# trajectory_tracker.py
"""Trajectory tracker for the Crazyflie controller.

Monitors the current state and advances to the next setpoint
in the trajectory once the current one is reached.
"""

import math
from trajectory_planner.trajectory import Trajectory


class TrajectoryTracker:
    """Tracks progress along a trajectory by checking if each
    setpoint has been reached within a given tolerance."""

    @property
    def trajectory_completed(self) -> bool:
        return self._trajectory_completed

    def __init__(self, trajectory: Trajectory,
                 position_tolerance: float = 0.02,
                 yaw_tolerance: float = 0.05):
        """
        Args:
            trajectory: The trajectory to track.
            position_tolerance: Distance threshold (meters) to consider a setpoint reached.
            yaw_tolerance: Yaw threshold (radians) to consider a setpoint reached.
        """
        self.trajectory = trajectory
        self.position_tolerance = position_tolerance
        self.yaw_tolerance = yaw_tolerance
        self._trajectory_completed = False

    def _position_error(self, state: dict) -> float:
        """Compute Euclidean distance between current state and current setpoint."""
        sp = self.trajectory.current_setpoint()
        pos_x, pos_y, pos_z = state["position"]
        dx = pos_x  - sp.x
        dy = pos_y  - sp.y
        dz = pos_z - sp.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

    def _yaw_error(self, state: dict) -> float:
        """Compute absolute yaw error between current state and current setpoint."""
        sp = self.trajectory.current_setpoint()
        _, _, yaw = state["attitude"]
        return abs(yaw - sp.yaw)

    def is_setpoint_reached(self, state: dict) -> bool:
        """Check if the current setpoint is reached within tolerances."""
        return (self._position_error(state) < self.position_tolerance
                and self._yaw_error(state) < self.yaw_tolerance)

    def update(self, state: dict, sim_time: float) -> dict:
        """Check state against current setpoint and advance if reached.
        Args:
            state: Current state dictionary.
            sim_time: Current simulation time in seconds.
        Returns:
            The current reference setpoint as a dictionary.
        """
        if self.is_setpoint_reached(state):
            if not self.trajectory.is_complete():
                sp = self.trajectory.current_setpoint()
                print(f"Setpoint {self.trajectory.current_index + 1} "
                  f"(x={sp.x}, y={sp.y}, z={sp.z}) "
                  f"reached at time {sim_time:.2f}s.")
                self.trajectory.advance()
                
            elif not self._trajectory_completed:
                sp = self.trajectory.current_setpoint()
                print(f"Setpoint {self.trajectory.current_index + 1} "
                    f"(x={sp.x}, y={sp.y}, z={sp.z}) "
                    f"reached at time {sim_time:.2f}s.")
                print(f"Trajectory completed at time {sim_time:.2f}s.")
                self._trajectory_completed = True
        return self.trajectory.current_setpoint().to_dict()
    
    
