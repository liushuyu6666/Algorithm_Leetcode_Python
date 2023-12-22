class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left, right = 0, 1  # [left, right)
        queue = [s[0]]  # `i` + left = curr_index in s
        longest = 1

        while right < len(s):
            if s[right] not in queue:
                queue.append(s[right])
                longest = max(longest, len(queue))
            else:
                i = queue.index(s[right])
                left = left + i + 1
                # update queue
                queue = queue[i + 1:]
                queue.append(s[right])
                longest = max(longest, len(queue))
            right += 1

        return longest

