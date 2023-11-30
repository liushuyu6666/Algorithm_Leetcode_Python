from typing import List


class CoinChangeDP:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp: List[int] = [10 ** 4 + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] < 10 ** 4 + 1 else -1


