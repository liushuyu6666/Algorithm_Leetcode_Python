from typing import List


class MinimizeTheMaximumOfTwoArrays:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [left, right)
        left, right, val, ans = 0, 1, nums[0], 10 ** 5 + 1

        while left <= right <= len(nums):
            if val < target:
                if right == len(nums):
                    break
                val += nums[right]
                right += 1
            elif val >= target:
                ans = min(ans, right - left)
                val -= nums[left]
                left += 1

        return ans if ans != 10 ** 5 + 1 else 0


