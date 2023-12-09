from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def dfs(left: int, right: int) -> int:
            if left == right:  # end condition: left == right
                return nums[left]

            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                # Update Right Pointer: Ensure strict mode (right = mid) as nums[mid] is possible the minimum value.
                return dfs(left, mid)
            elif nums[mid] > nums[right]:
                # Update Left Pointer: Employ strict mode (left = mid + 1) as nums[mid] is not the minimum value.
                return dfs(mid + 1, right) # update the left pointer: left = mid + 1, strict
            else:
                return min(dfs(left, mid), dfs(mid + 1, right))

        return dfs(0, len(nums) - 1)

