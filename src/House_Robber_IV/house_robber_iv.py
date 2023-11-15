import math
from typing import List


class HouseRobberIV:
    def minCapability(self, nums: List[int], k: int) -> int:

        def check(x: int) -> int:
            visited, count = False, 0
            for num in nums:
                if num <= x and visited is False:
                    visited, count = True, count + 1
                else:
                    visited = False
            return count

        left, right = min(nums), max(nums)
        while left <= right:
            middle = math.floor((left + right) / 2)
            if check(middle) >= k:
                right = middle - 1
            else:
                left = middle + 1

        return left
