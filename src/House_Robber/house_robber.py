from typing import List


class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        best_robbery: List[int] = [0, 0]
        house_size: int = len(nums)

        for i in range(house_size):
            rob_curr: int = best_robbery[-2] + nums[i]
            no_rob: int = best_robbery[-1]
            best_robbery.append(max(rob_curr, no_rob))

        return best_robbery[-1]
