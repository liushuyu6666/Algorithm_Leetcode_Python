from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        packed = list(map(set, zip(*strs)))
        s = ""
        for char_set in packed:
            if len(char_set) == 1:
                s += list(char_set)[0]
            else:
                break
        return s


if __name__ == '__main__':
    solution = Solution()
    prefix = solution.longestCommonPrefix(["flower", "flow", "flight"])
    print(prefix)
