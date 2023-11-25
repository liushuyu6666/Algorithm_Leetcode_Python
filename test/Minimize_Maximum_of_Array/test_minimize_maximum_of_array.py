import unittest

from src.Minimize_Maximum_of_Array.minimize_maximum_of_array import MinimizeMaximumOfArray


class TestMinimizeMaximumOfArray(unittest.TestCase):
    def test_rob(self):
        minimize = MinimizeMaximumOfArray()

        nums1 = [3, 7, 1, 6]
        self.assertEqual(minimize.minimizeArrayValue(nums1), 5)

        nums2 = [10, 1]
        self.assertEqual(minimize.minimizeArrayValue(nums2), 10)


if __name__ == "__main__":
    unittest.main()
