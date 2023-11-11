from typing import List


class MaximizeTheMinimumPoweredCity:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        station_size: int = len(stations)

        # get powers by prefix sum
        curr_sum = 0
        prefix_sum = []
        for station in stations:
            curr_sum += station
            prefix_sum.append(curr_sum)
        # windows range: [i - r, i + r]
        powers = [prefix_sum[
                      min(i + r, station_size - 1)] -
                    (0 if (i - r - 1) < 0 else prefix_sum[max(i - r - 1, 0)])
                  for i in range(station_size)]

        # differences array
        power_diffs = [powers[0]] + [powers[i] - powers[i - 1] for i in range(1, station_size)]

        def build_stations(diffs: List[int], loc: int, num: int) -> None:
            diffs[loc] += num
            if loc + 2 * r + 1 < station_size:
                diffs[loc + 2 * r + 1] -= num

        def check(x: int) -> bool:
            curr_power, count = 0, 0
            power_diffs_copy = power_diffs[:]

            for i in range(station_size):
                curr_power += power_diffs_copy[i]
                if curr_power < x:
                    need = x - curr_power
                    build_stations(power_diffs_copy, i, need)
                    curr_power = x
                    count += need
                    if count > k:
                        return False

            return count <= k

        left, right = min(powers), max(powers) + k
        while left <= right:
            middle = (left + right) // 2
            if check(middle):
                left = middle + 1
            else:
                right = middle - 1
        return right
