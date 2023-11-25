import unittest

from src.Maximum_Tastiness_of_Candy_Basket.maximum_tastiness_of_candy_basket import MaximumTastinessOfCandyBasket


class TestMaximumTastinessOfCandyBasket(unittest.TestCase):
    def test_tastiness(self):
        solution = MaximumTastinessOfCandyBasket()

        price, k = [13, 5, 1, 8, 21, 2], 3
        self.assertEqual(solution.maximumTastiness(price, k), 8)

        price, k = [1, 3, 1], 2
        self.assertEqual(solution.maximumTastiness(price, k), 2)

        price, k = [7, 7, 7, 7], 2
        self.assertEqual(solution.maximumTastiness(price, k), 0)


if __name__ == "__main__":
    unittest.main()
