"""
Pick your solution to one of the exercises in this module. Design tests for this solution and write tests using
unittest library.
"""

from lesson_7.task_2 import make_country
import unittest


class MakeCountryTestCase(unittest.TestCase):

    def test_make_country(self):
        country = make_country('Canada', 'Ottawa')
        self.assertEqual(country, {'country_name': 'Canada', 'capital': 'Ottawa'})
        self.assertNotEqual(country, {'country_name': 'Canada', 'capital': 'Warsaw'})
        self.assertNotEqual(country, {'country_name': 'Canada', 'capital': 'Ottawa'})


if __name__ == '__main__':
    unittest.main()
