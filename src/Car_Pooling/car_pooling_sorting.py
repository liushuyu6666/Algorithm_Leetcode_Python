from typing import List


class CarPoolingSorting:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        get_in = [[trip[1], trip[0]] for trip in trips]
        get_out = [[trip[2], trip[0] * -1] for trip in trips]

        pick_up_nums = get_in + get_out

        pick_up_nums.sort(key=lambda x: (x[0], x[1]))

        passagers = 0
        while pick_up_nums:
            passagers += pick_up_nums.pop(0)[1]
            if passagers > capacity:
                return False
        return True
