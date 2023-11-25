import unittest

from src.Minimize_the_Maximum_Difference_of_Pairs.minimize_the_maximum_difference_of_pairs import \
    MinimizeTheMaximumDifferenceOfPairs


class TestMinimizeTheMaximumDifferenceOfPairs(unittest.TestCase):
    def test_rob(self):
        minimize = MinimizeTheMaximumDifferenceOfPairs()

        nums, p = [10, 1, 2, 7, 1, 3], 2
        self.assertEqual(minimize.minimizeMax(nums, p), 1)

        nums, p = [4, 2, 1, 2], 1
        self.assertEqual(minimize.minimizeMax(nums, p), 0)

        nums, p = [0, 5, 3, 4], 0
        self.assertEqual(minimize.minimizeMax(nums, p), 0)


if __name__ == "__main__":
    unittest.main()
