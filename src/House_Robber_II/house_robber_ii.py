from typing import List


class HouseRobberII:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        best_robbery_skip_first: List[int] = [0, 0]
        best_robbery_skip_last: List[int] = [0, nums[0]]
        house_size: int = len(nums)

        # Skip the first house
        for i in range(1, house_size):
            rob_curr: int = nums[i] + best_robbery_skip_first[-2]
            skip_curr: int = best_robbery_skip_first[-1]
            best_robbery_skip_first.append(max(rob_curr, skip_curr))

        # Rob the first house
        for i in range(1, house_size - 1):
            rob_curr: int = nums[i] + best_robbery_skip_last[-2]
            skip_curr: int = best_robbery_skip_last[-1]
            best_robbery_skip_last.append(max(rob_curr, skip_curr))

        return max(best_robbery_skip_last[-1], best_robbery_skip_first[-1])

