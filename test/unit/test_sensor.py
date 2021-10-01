import unittest

from sensor.temperature import TemperatureSensor

class TestTemperatureSensor(unittest.TestCase):
    def test_init_sensor(self):
        temperature_sensor = TemperatureSensor('test', 'metric')
        self.assertTrue(hasattr(temperature_sensor, 'location'))
        self.assertEqual(temperature_sensor.location, 'test')
        self.assertEqual(temperature_sensor.measurement_unit, 'C')

    def test_get_temperature(self):
        temperature_sensor = TemperatureSensor('test', 'metric')
        current_temperature, units = temperature_sensor.get_temperature()
        self.assertEqual(units, "C")
        self.assertTrue(-70 < current_temperature < 70)

