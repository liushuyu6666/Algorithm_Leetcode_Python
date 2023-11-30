from functools import cache
from typing import List


class CoinChangeRecursionDFS:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def min_coins(money: int) -> int:
            if money < 0:
                return -1
            elif money == 0:
                return 0

            ans = 10 ** 5
            for coin in coins:
                prev_min_coin = min_coins(money - coin)
                if prev_min_coin == -1:
                    continue
                ans = min(ans, prev_min_coin + 1)

            return ans if ans < 10 ** 5 else -1

        return min_coins(amount)
