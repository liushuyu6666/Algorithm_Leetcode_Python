from typing import List


class MagneticForceBetweenTwoBalls:
    def maxDistance(self, position: List[int], m: int) -> int:
        # x: the minimum magnetic force
        def check(diffs: List[int], x: int) -> bool:
            count, dist = 1, 0
            for diff in diffs:
                dist += diff
                if dist >= x:
                    count += 1
                    dist = 0
                if count >= m:
                    return True
            return count >= m

        diffs: List[int] = []
        sorted_positions = sorted(position)
        for i in range(1, len(position)):
            diffs.append(abs(sorted_positions[i] - sorted_positions[i - 1]))

        # left, right stands for the initial least and most magnetic force
        left, right = min(diffs), sum(diffs)
        while left <= right:
            middle = (left + right) // 2
            if check(diffs, middle):
                left = middle + 1
            else:
                right = middle - 1

        return right
