import unittest

from src.Coin_Change_II.coin_change_ii_dp import CoinChangeIIDP


class TestCoinChangeII(unittest.TestCase):
    def test_coin_change_ii_dp(self):
        coin = CoinChangeIIDP()

        amount, coins = 5, [1, 2, 5]
        self.assertEqual(coin.coinChange(amount, coins), 4)

        amount, coins = 3, [2]
        self.assertEqual(coin.coinChange(amount, coins), 0)

        amount, coins = 10, [10]
        self.assertEqual(coin.coinChange(amount, coins), 1)


if __name__ == "__main__":
    unittest.main()
