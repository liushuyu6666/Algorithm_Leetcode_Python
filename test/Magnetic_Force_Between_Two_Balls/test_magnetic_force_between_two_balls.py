import unittest

from src.Magnetic_Force_Between_Two_Balls.magnetic_force_between_two_balls import MagneticForceBetweenTwoBalls


class TestMagneticForceBetweenTwoBalls(unittest.TestCase):
    def test_rob(self):
        solution = MagneticForceBetweenTwoBalls()

        position, m = [1, 2, 3, 4, 7], 3
        self.assertEqual(solution.maxDistance(position, m), 3)

        position, m = [5, 4, 3, 2, 1, 1000000000], 2
        self.assertEqual(solution.maxDistance(position, m), 1000000000 - 1)


if __name__ == "__main__":
    unittest.main()
