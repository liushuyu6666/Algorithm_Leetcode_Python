import unittest

from src.House_Robber_IV.house_robber_iv import HouseRobberIV


class TestHouseRobberIV(unittest.TestCase):
    def test_rob(self):
        robber = HouseRobberIV()

        nums1, k = [2, 3, 5, 9], 2
        self.assertEqual(robber.minCapability(nums1, k), 5)

        nums2, k = [2, 7, 9, 3, 1], 2
        self.assertEqual(robber.minCapability(nums2, k), 2)


if __name__ == "__main__":
    unittest.main()
