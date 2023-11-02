from functools import cache
from typing import List


class HouseRobberCached:
    def rob(self, nums: List[int]) -> int:
        house_size: int = len(nums)

        @cache
        def dp(n: int) -> int:
            if n >= house_size:
                return 0

            return max(dp(n + 1), nums[n] + dp(n + 2))

        return dp(0)

