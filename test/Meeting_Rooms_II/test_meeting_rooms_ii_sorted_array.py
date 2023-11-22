import unittest

from src.Meeting_Rooms_II.meeting_rooms_ii_sorted_array import MeetingRoomsIISortedArray


class TestMeetingRoomsII(unittest.TestCase):
    def test_meeting_room(self):
        solution = MeetingRoomsIISortedArray()

        intervals = [[0, 30], [5, 10], [15, 20]]
        self.assertEqual(solution.minMeetingRooms(intervals), 2)

        intervals = [[7, 10], [2, 4]]
        self.assertEqual(solution.minMeetingRooms(intervals), 1)


if __name__ == "__main__":
    unittest.main()
