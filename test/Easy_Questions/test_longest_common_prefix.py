import unittest
from src.Easy_Questions.longest_common_prefix import Solution


class TestLongestCommonPrefix(unittest.TestCase):
    def test_longest_common_prefix(self):
        solution = Solution()

        self.assertEqual(solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
