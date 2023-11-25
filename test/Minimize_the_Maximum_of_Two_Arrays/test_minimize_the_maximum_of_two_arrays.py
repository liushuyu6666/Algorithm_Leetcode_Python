import unittest

from src.Minimize_the_Maximum_of_Two_Arrays.minimize_the_maximum_of_two_arrays import MinimizeTheMaximumOfTwoArrays


class TestMinimizeMaximumOfArray(unittest.TestCase):
    def test_rob(self):
        minimize = MinimizeTheMaximumOfTwoArrays()

        divisor1, divisor2, uniqueCnt1, uniqueCnt2 = 2, 7, 1, 3
        self.assertEqual(minimize.minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2), 4)

        divisor1, divisor2, uniqueCnt1, uniqueCnt2 = 3, 5, 2, 1
        self.assertEqual(minimize.minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2), 3)

        divisor1, divisor2, uniqueCnt1, uniqueCnt2 = 2, 4, 8, 2
        self.assertEqual(minimize.minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2), 15)

        divisor1, divisor2, uniqueCnt1, uniqueCnt2 = 5, 2, 2, 20
        self.assertEqual(minimize.minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2), 39)


if __name__ == "__main__":
    unittest.main()
