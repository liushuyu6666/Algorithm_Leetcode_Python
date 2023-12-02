from typing import List


class MinHeap:
    def __init__(self, nums: List[List[int]]):
        self.size = len(nums)
        self.heap = [[0, 0]] + nums

        i = self.size // 2 + 1
        while i > 0:
            self.sink(i)
            i -= 1

    def swap(self, i: int, j: int) -> None:
        temp: List[int] = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def swim(self, curr_index: int) -> None:
        parent_index = curr_index // 2

        if curr_index <= 0 or curr_index > self.size or parent_index <= 0:
            return None

        while parent_index > 0:
            if self.heap[curr_index][0] < self.heap[parent_index][0]:
                self.swap(parent_index, curr_index)
            curr_index = parent_index
            parent_index = curr_index // 2

    def find_smaller_child(self, curr_index: int) -> int or None:
        left_child, right_child = curr_index * 2, curr_index * 2 + 1

        if curr_index <= 0 or curr_index > self.size or left_child > self.size:
            return None

        return left_child if right_child > self.size or \
                             self.heap[left_child][0] <= self.heap[right_child][0] else right_child

    def sink(self, curr_index: int) -> None:
        child_index = self.find_smaller_child(curr_index)

        if curr_index <= 0 or curr_index > self.size or child_index is None:
            return None

        while child_index is not None:
            if self.heap[child_index][0] < self.heap[curr_index][0]:
                self.swap(curr_index, child_index)
            curr_index = child_index
            child_index = self.find_smaller_child(curr_index)

    def push(self, new_entry: List[int]) -> None:
        self.size += 1
        self.heap.insert(self.size, new_entry)
        self.swim(self.size)

    def pop(self) -> List[int]:
        top = self.heap[1]
        self.swap(1, self.size)
        self.size -= 1
        self.sink(1)

        return top

    def top(self) -> List[int]:
        return self.heap[1]


class CarPoolingMinHeap:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        get_offs = [[trip[2], trip[0]] for trip in trips]  # [drop off location, The number of leaving passengers]

        min_heap = MinHeap(get_offs)

        passengers = 0
        for num, get_in_location, _ in trips:
            passengers += num
            while get_in_location >= min_heap.top()[0]:
                get_off = min_heap.pop()
                passengers -= get_off[1]
            if passengers > capacity:
                return False

        return True
