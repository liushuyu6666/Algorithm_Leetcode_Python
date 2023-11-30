from typing import List


class CoinChangeBitManipulation:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount === 0
        if not amount:
            return 0

        amount = 1 << amount

        step = 0
        while amount:
            temp = 0
            step += 1
            for coin in coins:
                temp |= amount >> coin
                if temp & 1:
                    return step
            amount = temp

        return -1
