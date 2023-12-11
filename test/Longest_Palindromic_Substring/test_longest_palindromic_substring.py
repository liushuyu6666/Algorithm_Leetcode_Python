import unittest
from src.Longest_Palindromic_Substring.longest_palindromic_substring import LongestPalindromicSubstring

class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_palindromic(self):
        solution = LongestPalindromicSubstring()

        s = "aacabdkacaa"
        self.assertEqual(solution.longestPalindrome(s), "aca")


if __name__ == "__main__":
    unittest.main()