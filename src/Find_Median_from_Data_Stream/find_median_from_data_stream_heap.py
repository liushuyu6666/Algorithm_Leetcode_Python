from typing import List


class MinHeap:
    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.heap: List[int] = [0] + nums

        i = self.size // 2
        while i > 0:
            self.sink(i)
            i -= 1

    def swap(self, i: int, j: int) -> None:
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def swim(self, curr_index: int) -> None:
        parent_index = curr_index // 2

        # in swim and find_smaller_child, always remember to check both boundary of curr_index
        if parent_index <= 0 or curr_index <= 0 or curr_index > self.size:
            return None

        while parent_index > 0:
            if self.heap[parent_index] > self.heap[curr_index]:
                self.swap(parent_index, curr_index)
            curr_index = parent_index
            parent_index = curr_index // 2

    def find_smaller_child(self, curr_index: int) -> int or None:
        left_child, right_child = curr_index * 2, curr_index * 2 + 1

        if curr_index <= 0 or curr_index > self.size or left_child > self.size:
            return None

        return left_child if right_child > self.size or self.heap[left_child] <= self.heap[right_child] else right_child

    def sink(self, curr_index: int) -> None:
        child_index = self.find_smaller_child(curr_index)

        if curr_index <= 0 or curr_index > self.size or not child_index:
            return None

        while child_index:
            if self.heap[child_index] < self.heap[curr_index]:
                self.swap(child_index, curr_index)
            curr_index = child_index
            child_index = self.find_smaller_child(curr_index)

    def push(self, new_num: int) -> None:
        self.size += 1
        self.heap.append(new_num)
        self.swim(self.size)

    def pop(self) -> int:
        self.swap(1, self.size)
        pop_out = self.heap.pop()
        self.size -= 1
        self.sink(1)
        return pop_out

    def top(self) -> int:
        return self.heap[1]


class MaxHeap:
    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.heap: List[int] = [0] + nums

        i = self.size // 2
        while i > 0:
            self.sink(i)
            i -= 1

    def swap(self, i: int, j: int) -> None:
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def swim(self, curr_index: int) -> None:
        parent_index = curr_index // 2

        if parent_index <= 0 or curr_index <= 0 or curr_index > self.size:
            return None

        while parent_index > 0:
            if self.heap[parent_index] < self.heap[curr_index]:
                self.swap(parent_index, curr_index)
            curr_index = parent_index
            parent_index = curr_index // 2

    def find_larger_child(self, curr_index: int) -> int or None:
        left_child, right_child = curr_index * 2, curr_index * 2 + 1

        if curr_index <= 0 or curr_index > self.size or left_child > self.size:
            return None

        return left_child if right_child > self.size or self.heap[left_child] >= self.heap[right_child] else right_child

    def sink(self, curr_index: int) -> None:
        child_index = self.find_larger_child(curr_index)

        if curr_index <= 0 or curr_index > self.size or not child_index:
            return None

        while child_index:
            if self.heap[child_index] > self.heap[curr_index]:
                self.swap(child_index, curr_index)
            curr_index = child_index
            child_index = self.find_larger_child(curr_index)

    def push(self, new_num: int) -> None:
        self.size += 1
        self.heap.append(new_num)
        self.swim(self.size)

    def pop(self) -> int:
        self.swap(1, self.size)
        pop_out = self.heap.pop()
        self.size -= 1
        self.sink(1)
        return pop_out

    def top(self) -> int:
        return self.heap[1]


class MedianFinderHeap:

    def __init__(self):
        self.less_queue = MaxHeap([])
        self.larger_queue = MinHeap([])

    def addNum(self, num: int) -> None:
        if self.less_queue.size == 0 and self.larger_queue.size == 0:
            self.less_queue.push(num)
            return

        if num > self.findMedian():
            self.larger_queue.push(num)
        else:
            self.less_queue.push(num)

        if self.less_queue.size - 1 > self.larger_queue.size:
            max_value = self.less_queue.pop()
            self.larger_queue.push(max_value)
        elif self.larger_queue.size > self.less_queue.size:
            min_value = self.larger_queue.pop()
            self.less_queue.push(min_value)

    def findMedian(self) -> float:
        if self.less_queue.size == self.larger_queue.size:
            return (self.less_queue.top() + self.larger_queue.top()) / 2
        else:
            return self.less_queue.top()
