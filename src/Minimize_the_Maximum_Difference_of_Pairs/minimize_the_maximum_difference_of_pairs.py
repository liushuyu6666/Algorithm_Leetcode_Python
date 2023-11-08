from typing import List


class MinimizeTheMaximumDifferenceOfPairs:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        def check(x: int, differences: List[int]) -> bool:
            count, visited = 0, False

            for difference in differences:
                if visited is False and difference <= x:
                    count += 1
                    visited = True
                else:
                    visited = False

                if count >= p:
                    return True

            return count >= p

        sorted_nums = sorted(nums)  # ascending
        diffs = []

        for i in range(1, len(sorted_nums)):
            diffs.append(sorted_nums[i] - sorted_nums[i - 1])

        left, right = min(diffs), max(diffs)
        while left <= right:
            middle = (left + right) // 2
            if check(middle, diffs):
                right = middle - 1
            else:
                left = middle + 1

        return left
