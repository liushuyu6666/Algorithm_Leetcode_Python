from typing import List


class MaximumTastinessofCandyBasket:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # x: possible tastiness
        # diffs: sorted differences
        def check(diffs: List[int], x: int) -> bool:
            count, acc_tastiness = 1, 0
            for diff in diffs:
                acc_tastiness += diff
                if acc_tastiness >= x:
                    count += 1
                    acc_tastiness = 0
                if count >= k:
                    return True
            return count >= k

        price.sort()
        diffs = [abs(price[i] - price[i - 1]) for i in range(1, len(price))]

        # binary search
        left, right = min(diffs), sum(diffs)
        while left <= right:
            middle = (left + right) // 2
            if check(diffs, middle):
                left = middle + 1
            else:
                right = middle - 1

        return max(right, 0)

