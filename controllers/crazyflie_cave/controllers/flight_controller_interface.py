from abc import ABC, abstractmethod
from typing import List, Dict

class FlightController(ABC):

    @abstractmethod
    def compute_motor_commands(
        self,
        state: Dict,
        reference: Dict,
        debug: bool = False,
    ) -> List[float]:
        """
        Returns:
            list of motor velocities [m1, m2, m3, m4]
        """
        pass
