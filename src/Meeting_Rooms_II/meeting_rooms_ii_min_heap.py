from typing import List


class MinHeap:
    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.heap = [0] + nums[:]

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

        if curr_index > self.size or curr_index <= 0 or parent_index <= 0:
            return None

        while parent_index > 0:
            if self.heap[curr_index] < self.heap[parent_index]:
                self.swap(curr_index, parent_index)
            curr_index = parent_index
            parent_index = curr_index // 2

    def find_smaller_child(self, curr_index: int) -> int or None:
        left_child, right_child = curr_index * 2, curr_index * 2 + 1

        if curr_index > self.size or curr_index <= 0 or left_child > self.size:
            return None

        return left_child if right_child > self.size \
                             or self.heap[left_child] < self.heap[right_child] else right_child

    def sink(self, curr_index) -> None:
        child_index = self.find_smaller_child(curr_index)

        if curr_index > self.size or curr_index <= 0 or child_index is None:
            return None

        while child_index is not None:
            if self.heap[child_index] < self.heap[curr_index]:
                self.swap(child_index, curr_index)
            curr_index = child_index
            child_index = self.find_smaller_child(curr_index)

    def push(self, new_num: int) -> None:
        self.size += 1
        self.heap.insert(self.size, new_num)
        self.swim(self.size)

    def pop(self) -> None:
        self.swap(1, self.size)
        self.size -= 1
        self.sink(1)

    def top(self) -> int:
        return self.heap[1]


class MeetingRoomsIIMinHeap:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        occupied_rooms = MinHeap([])
        occupied_rooms.push(intervals[0][1])

        for meeting in intervals[1:]:
            start_time = meeting[0]
            end_time = meeting[1]
            if occupied_rooms.top() <= start_time:
                occupied_rooms.pop()
            occupied_rooms.push(end_time)

        return occupied_rooms.size
