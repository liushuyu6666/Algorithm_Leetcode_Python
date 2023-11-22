import random
from typing import List


def quick_select(nums: List[int], k: int) -> int:
    pivot: int = random.choice(nums)

    larger, equal, smaller = [], [], []
    for num in nums:
        if num > pivot:
            larger.append(num)
        elif num < pivot:
            smaller.append(num)
        else:
            equal.append(num)

    if len(larger) >= k:  # The k-th value is located in the "larger" bucket.
        return quick_select(larger, k)
    elif len(nums) - len(smaller) < k:  # The k-th value is located in the "smaller" bucket.
        return quick_select(smaller, k - len(larger) - len(equal))
    else:  # The k-th value is located in the "equal" bucket.
        return pivot


class KthLargestElementInAnArrayQuickSelect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quick_select(nums, k)
