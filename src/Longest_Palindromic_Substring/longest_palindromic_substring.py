from typing import List


class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        dp: List[List[int]] = [[False] * len(s)] * len(s)

        palindrome = ''
        for j in range(len(s)):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = True
                    if j - i + 1 > len(palindrome):
                        palindrome = s[i: j+1]
                elif j - i == 1:
                    dp[i][j] = (s[i] == s[j])
                    if dp[i][j] and j - i + 1 > len(palindrome):
                        palindrome = s[i: j+1]
                elif j - i > 1:
                    dp[i][j] = (dp[i+1][j-1]) and (s[i] == s[j])
                    if dp[i][j] and j - i + 1 > len(palindrome):
                        palindrome = s[i: j + 1]

        return palindrome
