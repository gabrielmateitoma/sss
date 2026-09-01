import unittest

from p4_race_fixture import race_value


class TestRaceValue(unittest.TestCase):
    def test_h2_value(self):
        self.assertEqual(race_value(), "H2")


if __name__ == "__main__":
    unittest.main()
