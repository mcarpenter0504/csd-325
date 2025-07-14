import unittest
from city_functions import format_city_country

class CityCountryTestCase(unittest.TestCase):
    # Tests for the format_city_country function.

    def test_city_country(self):
        formatted = format_city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()