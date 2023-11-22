from typing import List


class MeetingRoomsIISortedArray:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        come_in = [interval[0] for interval in intervals]
        come_out = [interval[1] for interval in intervals]
        come_in.sort()
        come_out.sort()

        rooms = 0
        min_rooms = 0
        i, j = 0, 0
        # if neither come_in and come_out are empty
        while i < len(come_in) and j < len(come_out):
            if come_in[i] < come_out[j]:
                rooms += 1
                min_rooms = max(min_rooms, rooms)
                i += 1
            elif come_out[j] < come_in[i]:
                rooms -= 1
                j += 1
            else:
                i += 1
                j += 1

        return min_rooms
