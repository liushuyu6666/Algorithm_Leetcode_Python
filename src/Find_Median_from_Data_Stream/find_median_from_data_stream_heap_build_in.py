import heapq


class MedianFinderHeapBuildIn:

    def __init__(self):
        self.less_queue = []  # max heap
        self.larger_queue = []  # min heap

    def addNum(self, num: int) -> None:
        if len(self.less_queue) == len(self.larger_queue):
            min_val = heapq.heappushpop(self.larger_queue, num)
            heapq.heappush(self.less_queue, -min_val)
        else:
            max_val = -heapq.heappushpop(self.less_queue, -num)
            heapq.heappush(self.larger_queue, max_val)

    def findMedian(self) -> float:
        if len(self.less_queue) == len(self.larger_queue):
            return (self.larger_queue[0] - self.less_queue[0]) / 2
        else:
            return - self.less_queue[0]
