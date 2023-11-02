import unittest

from src.House_Robber.house_robber import HouseRobber


class TestHouseRobber(unittest.TestCase):
    def test_rob(self):
        robber = HouseRobber()

        # Test case 1: Example case
        nums1 = [1, 2, 3, 1]
        self.assertEqual(robber.rob(nums1), 4)

        # Test case 2: Edge case with an empty list
        nums2 = []
        self.assertEqual(robber.rob(nums2), 0)

        # Test case 3: Edge case with a single house
        nums3 = [2]
        self.assertEqual(robber.rob(nums3), 2)

        # Test case 4: All houses can be robbed
        nums4 = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235,
                 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
        self.assertEqual(robber.rob(nums4), 12)


if __name__ == "__main__":
    unittest.main()
