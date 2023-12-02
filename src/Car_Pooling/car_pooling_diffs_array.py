from typing import List


class CarPoolingDifferencesArray:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        distance = max([trip[2] for trip in trips])
        pick_up_nums = [0] * (distance + 1)

        for trip in trips:
            pick_up_nums[trip[1]] += trip[0]
            pick_up_nums[trip[2]] -= trip[0]

        passengers = 0
        for pick_up_num in pick_up_nums:
            passengers += pick_up_num
            if passengers > capacity:
                return False

        return True

