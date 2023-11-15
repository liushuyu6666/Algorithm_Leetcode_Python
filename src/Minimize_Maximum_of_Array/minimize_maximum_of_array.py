import math
from typing import List


class MinimizeMaximumOfArray:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        def check(x: int) -> bool:
            accommodation = 0
            for num in nums:
                if num < x:
                    accommodation += x - num
                else:
                    accommodation -= num - x
                if accommodation < 0:
                    return False
            return True

        left, right = min(nums), max(nums)

        while left <= right:
            middle = math.floor((left + right) / 2)
            if check(middle):
                right = middle - 1
            else:
                left = middle + 1

        return left
