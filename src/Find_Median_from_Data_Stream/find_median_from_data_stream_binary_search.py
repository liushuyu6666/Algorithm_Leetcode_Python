from typing import List


class MedianFinderBinarySearch:

    def __init__(self):
        self.less_queue: List[int] = []
        self.larger_queue: List[int] = []

    def addNum(self, num: int) -> None:
        if len(self.less_queue) == 0 and len(self.larger_queue) == 0:
            self.less_queue.append(num)
            return

        if num > self.findMedian():
            index = self.binary_search(num, self.larger_queue)
            self.larger_queue.insert(index, num)
        else:
            index = self.binary_search(num, self.less_queue)
            self.less_queue.insert(index, num)

        if len(self.less_queue) - 1 > len(self.larger_queue):
            largest = self.less_queue.pop()
            self.larger_queue.insert(0, largest)
        elif len(self.larger_queue) > len(self.less_queue):
            smallest = self.larger_queue.pop(0)
            self.less_queue.append(smallest)

    def findMedian(self) -> float:

        if len(self.less_queue) == len(self.larger_queue):
            return (self.less_queue[-1] + self.larger_queue[0]) / 2

        return self.less_queue[-1]

    def binary_search(self, num: int, queue: List[int]) -> int:
        left, right = 0, len(queue) - 1
        mid = (left + right) // 2

        while left <= right:
            if queue[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

            mid = (left + right) // 2

        # left points to the nearest larger value
        return left


