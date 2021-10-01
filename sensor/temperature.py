import random
from typing import Tuple


class TemperatureSensor():
    """A reusable temperature sensor."""
    def __init__(self, location, units):
        self.location = location
        self.measurement_unit = "C" if units == "metric" else "F"

    @property
    def _temperature(self):
        """Generate a random temperature.
        
        For the purposes of being a test Skill.
        """
        return random.randint(-70, 70)

    def get_temperature(self) -> tuple((int, str)):
        """Get the current temperature.
        
        Returns:
            (current temperature, measurement unit (C/F)
        """
        return self._temperature, self.measurement_unit



