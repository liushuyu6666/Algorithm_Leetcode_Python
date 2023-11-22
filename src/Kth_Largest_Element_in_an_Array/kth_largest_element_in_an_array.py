from typing import List


class MaxHeap:
    def __init__(self, arr: List[int]):
        self.heap = [0] + arr[:]  # shallow copy
        self.size = len(arr)

        curr_index = self.size // 2

        while curr_index > 0:
            self.sink(curr_index)
            curr_index -= 1

    def swap(self, i: int, j: int) -> None:
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def swim(self, curr_index: int) -> None:
        parent_index = curr_index // 2

        if curr_index > self.size or curr_index <= 0 or parent_index <= 0:
            return None

        while parent_index > 0:
            if self.heap[curr_index] > self.heap[parent_index]:
                self.swap(curr_index, parent_index)
            curr_index = parent_index
            parent_index = curr_index // 2

    def find_larger_child(self, curr_index: int) -> int or None:
        left_child, right_child = curr_index * 2, curr_index * 2 + 1

        if curr_index <= 0 or curr_index > self.size or left_child > self.size:
            return None

        return left_child if right_child > self.size or self.heap[left_child] > self.heap[right_child] \
            else right_child

    def sink(self, curr_index: int) -> None:
        child = self.find_larger_child(curr_index)

        if curr_index > self.size or curr_index <= 0 or child is None:
            return None

        while child is not None:
            if self.heap[child] > self.heap[curr_index]:
                self.swap(child, curr_index)
            curr_index = child
            child = self.find_larger_child(curr_index)

    def push(self, num: int) -> None:
        self.heap.append(num)
        self.size += 1
        self.swim(self.size)

    def pop(self) -> None:
        self.swap(1, self.size)
        self.size -= 1
        self.sink(1)

    def top(self) -> int:
        return self.heap[1]


class KthLargestElementInAnArray:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MaxHeap(nums)

        while k > 1:
            heap.pop()
            k -= 1

        return heap.top()
