from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def dfs(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                return dfs(left, mid)
            elif nums[mid] > nums[right]:
                return dfs(mid + 1, right)
            else:
                return min(dfs(left, mid), dfs(mid + 1, right))

        return dfs(0, len(nums) - 1)

