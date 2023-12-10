class Josephuse:
    def zero_indexed(self, num: int, target: int) -> int:
        def f(x: int, s: int) -> int:
            if s == num:
                return x

            index_in_upper_step = (x + target) % (s + 1)
            return f(index_in_upper_step, s + 1)

        return f(0, 1)

    def one_indexed(self, num: int, target: int) -> int:
        def f(x: int, s: int) -> int:
            if s == num:
                return x

            index_in_upper_step = (((x + target) - 1) % (s + 1)) + 1
            return f(index_in_upper_step, s + 1)

        return f(1, 1) - 1
