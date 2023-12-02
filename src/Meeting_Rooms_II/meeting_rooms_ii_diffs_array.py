from typing import List


class MeetingRoomsIIDiffsArray:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        final_time = max([interval[1] for interval in intervals])
        occupied_rooms = [0] * (final_time + 1)

        for start, end in intervals:
            occupied_rooms[start] += 1
            occupied_rooms[end] -= 1

        total_occupied_room, max_occupied_room = 0, 0
        for occupied_room in occupied_rooms:
            total_occupied_room += occupied_room
            max_occupied_room = max(max_occupied_room, total_occupied_room)

        return max_occupied_room
