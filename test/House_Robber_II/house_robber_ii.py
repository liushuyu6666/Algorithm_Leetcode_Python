import unittest

from src.House_Robber_II.house_robber_ii import HouseRobberII


class TestHouseRobber(unittest.TestCase):
    def test_rob(self):
        robber = HouseRobberII()

        nums1 = [2, 3, 2]
        self.assertEqual(robber.rob(nums1), 3)

        nums2 = []
        self.assertEqual(robber.rob(nums2), 0)

        nums3 = [1, 2, 3, 1]
        self.assertEqual(robber.rob(nums3), 4)

        nums4 = [1, 2, 3]
        self.assertEqual(robber.rob(nums4), 3)

        nums5 = [1]
        self.assertEqual(robber.rob(nums5), 1)


if __name__ == "__main__":
    unittest.main()
