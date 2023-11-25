import unittest

from src.Meeting_Rooms_II.meeting_rooms_ii_min_heap import MeetingRoomsIIMinHeap


class TestMeetingRoomsIIMinHeap(unittest.TestCase):
    def test_meeting_room(self):
        solution = MeetingRoomsIIMinHeap()

        intervals = [[0, 30], [5, 10], [15, 20]]
        self.assertEqual(solution.minMeetingRooms(intervals), 2)

        intervals = [[7, 10], [2, 4]]
        self.assertEqual(solution.minMeetingRooms(intervals), 1)

        intervals = [[13, 15], [1, 13]]
        self.assertEqual(solution.minMeetingRooms(intervals), 1)

        intervals = [[1, 5], [8, 9], [8, 9]]
        self.assertEqual(solution.minMeetingRooms(intervals), 2)


if __name__ == "__main__":
    unittest.main()
