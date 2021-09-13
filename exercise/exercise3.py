# give a string, find the length of substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str)->int:
        longest = 0
        start = 0
        char_map = {}
        for k, v in enumerate(s):
            if v in char_map:
                start = max(start, char_map[v] + 1)
            longest = max(longest, k - start + 1)


