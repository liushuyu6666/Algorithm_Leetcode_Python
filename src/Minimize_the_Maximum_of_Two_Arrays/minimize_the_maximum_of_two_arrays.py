import math


class MinimizeTheMaximumOfTwoArrays:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def check(x: int) -> bool:
            # least common multiple
            lcm = math.lcm(divisor1, divisor2)
            # accommodate in arr1 but not in arr2
            only_arr1 = x // divisor2 - x // lcm
            # accommodate in arr2 but not in arr1
            only_arr2 = x // divisor1 - x // lcm
            # accommodate in both
            both_arr = x - (x // divisor1 + x // divisor2 - x // lcm)
            # after consuming all only_arr1, arr1 still needs
            arr1_need_more = max(uniqueCnt1 - only_arr1, 0)
            # after consuming all only_arr2, arr2 still needs
            arr2_need_more = max(uniqueCnt2 - only_arr2, 0)

            return both_arr >= arr1_need_more + arr2_need_more

        left, right = 1, 2 * (10 ** 9)

        while left <= right:
            middle = (left + right) // 2
            if check(middle):
                right = middle - 1
            else:
                left = middle + 1

        return left
