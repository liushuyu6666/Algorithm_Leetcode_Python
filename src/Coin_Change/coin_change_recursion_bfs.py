import collections
from typing import List


class CoinChangeRecursionBFS:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = collections.deque()
        queue.append(amount)
        seen = set()

        step = -1
        while queue:
            step += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == 0:
                    return step
                if curr in seen:
                    continue
                seen.add(curr)
                queue.extend(
                    [curr - coin for coin in coins if curr - coin >= 0]
                )
        return -1





