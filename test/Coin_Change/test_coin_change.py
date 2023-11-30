import unittest

from src.Coin_Change.coin_change_recursion_dfs import CoinChangeRecursionDFS
from src.Coin_Change.coin_change_recursion_bfs import CoinChangeRecursionBFS
from src.Coin_Change.coin_change_dp import CoinChangeDP
from src.Coin_Change.coin_change_bit_manipulation import CoinChangeBitManipulation


class TestCoinChange(unittest.TestCase):
    def test_coin_change_recursion_dfs(self):
        coin = CoinChangeRecursionDFS()

        coins, amount = [1, 2, 5], 11
        self.assertEqual(coin.coinChange(coins, amount), 3)

        coins, amount = [2], 3
        self.assertEqual(coin.coinChange(coins, amount), -1)

        coins, amount = [1], 0
        self.assertEqual(coin.coinChange(coins, amount), 0)

    def test_coin_change_recursion_bfs(self):
        coin = CoinChangeRecursionBFS()

        coins, amount = [1, 2, 5], 11
        self.assertEqual(coin.coinChange(coins, amount), 3)

        coins, amount = [2], 3
        self.assertEqual(coin.coinChange(coins, amount), -1)

        coins, amount = [1], 0
        self.assertEqual(coin.coinChange(coins, amount), 0)

    def test_coin_change_dp(self):
        coin = CoinChangeDP()

        coins, amount = [1, 2, 5], 11
        self.assertEqual(coin.coinChange(coins, amount), 3)

        coins, amount = [2], 3
        self.assertEqual(coin.coinChange(coins, amount), -1)

        coins, amount = [1], 0
        self.assertEqual(coin.coinChange(coins, amount), 0)

    def test_coin_change_bit_manipulation(self):
        coin = CoinChangeBitManipulation()

        coins, amount = [1, 2, 5], 11
        self.assertEqual(coin.coinChange(coins, amount), 3)

        coins, amount = [2], 3
        self.assertEqual(coin.coinChange(coins, amount), -1)

        coins, amount = [1], 0
        self.assertEqual(coin.coinChange(coins, amount), 0)



if __name__ == "__main__":
    unittest.main()
